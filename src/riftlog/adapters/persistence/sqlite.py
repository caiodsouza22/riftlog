"""SQLite persistence for runs and step results."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from riftlog.domain.entities import JobRun, StepResult
from riftlog.domain.errors import RunMissing
from riftlog.domain.states import RunState, StepState


def _dt(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value)


def _iso(value: datetime | None) -> str | None:
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.isoformat()


class SqliteStore:
    def __init__(self, path: str | Path = ":memory:") -> None:
        self.path = str(path)
        self._conn = sqlite3.connect(self.path)
        self._conn.row_factory = sqlite3.Row
        self._setup()

    def _setup(self) -> None:
        self._conn.executescript(
            """
            create table if not exists runs (
                run_id text primary key,
                job text not null,
                state text not null,
                tenant_id text not null,
                created_at text not null,
                started_at text,
                finished_at text,
                trigger text not null,
                label text not null
            );
            create table if not exists step_results (
                run_id text not null,
                name text not null,
                state text not null,
                attempts integer not null,
                output_json text,
                error text not null,
                started_at text,
                finished_at text,
                log_text text not null,
                primary key (run_id, name)
            );
            """
        )
        self._conn.commit()

    def put(self, run: JobRun) -> JobRun:
        self._conn.execute(
            """
            insert or replace into runs (
                run_id, job, state, tenant_id, created_at, started_at,
                finished_at, trigger, label
            ) values (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                run.run_id,
                run.job,
                run.state.value,
                run.tenant_id,
                _iso(run.created_at),
                _iso(run.started_at),
                _iso(run.finished_at),
                run.trigger,
                run.label,
            ),
        )
        self._conn.execute("delete from step_results where run_id = ?", (run.run_id,))
        for result in run.results.values():
            self._conn.execute(
                """
                insert into step_results (
                    run_id, name, state, attempts, output_json, error,
                    started_at, finished_at, log_text
                ) values (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    run.run_id,
                    result.name,
                    result.state.value,
                    result.attempts,
                    json.dumps(result.output, default=str),
                    result.error,
                    _iso(result.started_at),
                    _iso(result.finished_at),
                    "\n".join(result.log_lines),
                ),
            )
        self._conn.commit()
        return run

    def get(self, run_id: str) -> JobRun:
        row = self._conn.execute("select * from runs where run_id = ?", (run_id,)).fetchone()
        if row is None:
            raise RunMissing(run_id)
        run = self._run_from(row)
        results = self._conn.execute(
            "select * from step_results where run_id = ? order by name",
            (run_id,),
        ).fetchall()
        run.results = {item["name"]: self._result_from(item) for item in results}
        return run

    def list(self, job: str | None = None, tenant_id: str | None = None) -> list[JobRun]:
        sql = "select * from runs"
        args: list[object] = []
        clauses: list[str] = []
        if job:
            clauses.append("job = ?")
            args.append(job)
        if tenant_id:
            clauses.append("tenant_id = ?")
            args.append(tenant_id)
        if clauses:
            sql += " where " + " and ".join(clauses)
        sql += " order by created_at, run_id"
        rows = self._conn.execute(sql, args).fetchall()
        return [self.get(row["run_id"]) for row in rows]

    def _run_from(self, row: sqlite3.Row) -> JobRun:
        return JobRun(
            run_id=row["run_id"],
            job=row["job"],
            state=RunState(row["state"]),
            created_at=_dt(row["created_at"]) or datetime.now(timezone.utc),
            tenant_id=row["tenant_id"],
            started_at=_dt(row["started_at"]),
            finished_at=_dt(row["finished_at"]),
            trigger=row["trigger"],
            label=row["label"],
        )

    def _result_from(self, row: sqlite3.Row) -> StepResult:
        output = json.loads(row["output_json"]) if row["output_json"] else None
        logs = [line for line in row["log_text"].split("\n") if line]
        return StepResult(
            name=row["name"],
            state=StepState(row["state"]),
            attempts=row["attempts"],
            output=output,
            error=row["error"],
            started_at=_dt(row["started_at"]),
            finished_at=_dt(row["finished_at"]),
            log_lines=logs,
        )
