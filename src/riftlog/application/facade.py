"""Application facade: load, run, persist. Keeps CLI thin."""

from __future__ import annotations

from pathlib import Path

from riftlog.adapters.yaml.loader import load_job
from riftlog.application.catalog import Catalog
from riftlog.application.engine import Engine
from riftlog.domain.entities import JobRun, JobSpec
from riftlog.ports.clock import Clock
from riftlog.ports.store import RunStore


class Orchestrator:
    """Load a spec, run it, optionally persist the snapshot."""

    def __init__(
        self,
        catalog: Catalog | None = None,
        clock: Clock | None = None,
        store: RunStore | None = None,
    ) -> None:
        self.engine = Engine(catalog=catalog, clock=clock)
        self.store = store

    def run_text(self, text: str, trigger: str = "manual") -> JobRun:
        from riftlog.adapters.yaml.loader import parse_job

        return self._persist(self.engine.run(parse_job(text), trigger=trigger))

    def run_path(self, path: str | Path, trigger: str = "manual") -> JobRun:
        return self._persist(self.engine.run(load_job(path), trigger=trigger))

    def run_spec(self, job: JobSpec, trigger: str = "manual") -> JobRun:
        return self._persist(self.engine.run(job, trigger=trigger))

    def _persist(self, run: JobRun) -> JobRun:
        if self.store is not None:
            return self.store.put(run)
        return run
