"""Fire scheduled jobs when Agenda matches clock.now()."""

from __future__ import annotations

from riftlog.adapters.persistence.memory import MemoryStore
from riftlog.adapters.time.clocks import WallClock
from riftlog.application.engine import Engine
from riftlog.cron.expr import Agenda
from riftlog.domain.entities import JobRun, JobSpec
from riftlog.ports.clock import Clock
from riftlog.ports.store import RunStore


class Scheduler:
    def __init__(
        self,
        engine: Engine | None = None,
        store: RunStore | None = None,
        clock: Clock | None = None,
    ) -> None:
        self.clock = clock or WallClock()
        self.engine = engine or Engine(clock=self.clock)
        self.store = store or MemoryStore()
        self._jobs: dict[str, JobSpec] = {}
        self._last: dict[str, str] = {}

    def add(self, job: JobSpec) -> None:
        if not job.schedule:
            raise ValueError(f"{job.name} has no schedule")
        Agenda(job.schedule)
        self._jobs[job.name] = job

    def tick(self) -> list[JobRun]:
        now = self.clock.now()
        stamp = now.replace(second=0, microsecond=0).isoformat()
        started: list[JobRun] = []
        for job in self._jobs.values():
            agenda = Agenda(job.schedule or "")
            if not agenda.matches(now):
                continue
            if self._last.get(job.name) == stamp:
                continue
            run = self.engine.run(job, trigger="agenda")
            self.store.put(run)
            self._last[job.name] = stamp
            started.append(run)
        return started

    def names(self) -> list[str]:
        return sorted(self._jobs)
