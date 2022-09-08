"""In-memory run history."""

from __future__ import annotations

from riftlog.domain.entities import JobRun
from riftlog.domain.errors import RunMissing


class MemoryStore:
    def __init__(self) -> None:
        self._runs: dict[str, JobRun] = {}

    def put(self, run: JobRun) -> JobRun:
        self._runs[run.run_id] = run
        return run

    def get(self, run_id: str) -> JobRun:
        if run_id not in self._runs:
            raise RunMissing(run_id)
        return self._runs[run_id]

    def list(self, job: str | None = None, tenant_id: str | None = None) -> list[JobRun]:
        rows = list(self._runs.values())
        if job:
            rows = [row for row in rows if row.job == job]
        if tenant_id:
            rows = [row for row in rows if row.tenant_id == tenant_id]
        rows.sort(key=lambda row: (row.created_at, row.run_id))
        return rows

    def drop(self, run_id: str) -> None:
        self._runs.pop(run_id, None)

    def clear(self) -> None:
        self._runs.clear()
