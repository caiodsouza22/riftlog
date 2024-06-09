"""Facade: load, run, store, schedule."""

from __future__ import annotations

from riftlog.adapters.persistence.memory import MemoryStore
from riftlog.adapters.time.clocks import WallClock
from riftlog.adapters.yaml.loader import load_job, parse_job
from riftlog.application.engine import Engine
from riftlog.application.scheduler import Scheduler
from riftlog.application.validate import validate_job
from riftlog.domain.entities import JobRun, JobSpec
from riftlog.ports.clock import Clock
from riftlog.ports.store import RunStore


class Pipeline:
    def __init__(self, store: RunStore | None = None, clock: Clock | None = None) -> None:
        self.clock = clock or WallClock()
        self.store = store or MemoryStore()
        self.engine = Engine(clock=self.clock)
        self.scheduler = Scheduler(self.engine, self.store, self.clock)
        self.jobs: dict[str, JobSpec] = {}

    def load(self, source: str) -> JobSpec:
        job = load_job(source) if "\n" not in source and not source.strip().startswith("name:") else parse_job(source)
        validate_job(job)
        self.jobs[job.name] = job
        if job.schedule:
            self.scheduler.add(job)
        return job

    def run(self, name: str, trigger: str = "manual") -> JobRun:
        job = self.jobs[name]
        record = self.engine.run(job, trigger=trigger)
        self.store.put(record)
        return record

    def get(self, run_id: str) -> JobRun:
        return self.store.get(run_id)

    def tick(self) -> list[JobRun]:
        return self.scheduler.tick()
