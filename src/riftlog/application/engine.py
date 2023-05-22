"""Run a job locally, in created/topo order, with retries."""

from __future__ import annotations

from uuid import uuid4

from riftlog.adapters.logging.buffer import LogBuf
from riftlog.adapters.time.clocks import WallClock
from riftlog.application.catalog import GLOBAL, Catalog
from riftlog.application.retry import RetryPlan
from riftlog.domain.entities import JobRun, JobSpec, StepResult, StepSpec
from riftlog.domain.errors import RetryGone
from riftlog.domain.graph import ready_names, topo_order
from riftlog.domain.states import RunState, StepState, TriggerKind
from riftlog.ports.clock import Clock


class Engine:
    def __init__(self, catalog: Catalog | None = None, clock: Clock | None = None) -> None:
        self.catalog = catalog or GLOBAL
        self.clock = clock or WallClock()

    def run(self, job: JobSpec, trigger: str = TriggerKind.MANUAL.value) -> JobRun:
        now = self.clock.now()
        record = JobRun(
            run_id=uuid4().hex[:12],
            job=job.name,
            state=RunState.RUNNING,
            created_at=now,
            tenant_id=job.tenant_id,
            started_at=now,
            trigger=trigger,
            label=job.label,
        )
        done: set[str] = set()
        failed = False
        order = topo_order(job)
        by_name = job.by_name()
        while len(done) < len(order) and not failed:
            batch = ready_names(job, done)
            if not batch:
                break
            cap = job.max_parallel if job.max_parallel > 0 else len(batch)
            for name in batch[:cap]:
                spec = by_name[name]
                result = self._run_step(spec)
                record.results[name] = result
                done.add(name)
                if result.state == StepState.FAILED:
                    failed = True
                    break
        record.finished_at = self.clock.now()
        record.state = RunState.FAILED if failed else RunState.OK
        if failed:
            for name in order:
                if name not in record.results:
                    record.results[name] = StepResult(name=name, state=StepState.SKIPPED)
        return record

    def _run_step(self, spec: StepSpec) -> StepResult:
        plan = RetryPlan(spec.retries, spec.retry_seconds)
        logs = LogBuf()
        last_error = ""
        started = self.clock.now()
        while True:
            try:
                fn = self.catalog.get(spec.call)
                output = fn(**spec.payload)
                logs.write(self.clock.now(), "info", f"{spec.name} ok")
                return StepResult(
                    name=spec.name,
                    state=StepState.OK,
                    attempts=plan.attempts + 1,
                    output=output,
                    started_at=started,
                    finished_at=self.clock.now(),
                    log_lines=list(logs.lines),
                )
            except Exception as exc:  # noqa: BLE001 — step sandbox
                last_error = str(exc) or exc.__class__.__name__
                logs.write(self.clock.now(), "error", last_error)
                if not plan.record_fail():
                    return StepResult(
                        name=spec.name,
                        state=StepState.FAILED,
                        attempts=plan.attempts,
                        error=last_error,
                        started_at=started,
                        finished_at=self.clock.now(),
                        log_lines=list(logs.lines),
                    )
        raise RetryGone(spec.name, plan.attempts, last_error)


def run_job(job: JobSpec, **kwargs: object) -> JobRun:
    allowed = {k: v for k, v in kwargs.items() if k in {"catalog", "clock"}}
    return Engine(**allowed).run(job)
