"""Pull work from a dispatch and run one step at a time."""

from __future__ import annotations

from riftlog.adapters.time.clocks import WallClock
from riftlog.application.catalog import GLOBAL, Catalog
from riftlog.application.engine import Engine
from riftlog.domain.entities import StepResult
from riftlog.ports.clock import Clock
from riftlog.workers.dispatch import Dispatch, Work


class Worker:
    def __init__(
        self,
        dispatch: Dispatch,
        catalog: Catalog | None = None,
        clock: Clock | None = None,
        queues: list[str] | None = None,
    ) -> None:
        self.dispatch = dispatch
        self.catalog = catalog or GLOBAL
        self.clock = clock or WallClock()
        self.queues = queues or ["default"]
        self._inner = Engine(self.catalog, self.clock)
        self.done: list[tuple[Work, StepResult]] = []

    def tick(self) -> StepResult | None:
        for name in self.queues:
            work = self.dispatch.take(name)
            if work is None:
                continue
            result = self._inner._run_step(work.step)
            self.done.append((work, result))
            return result
        return None

    def drain(self, steps: int = 32) -> list[StepResult]:
        out: list[StepResult] = []
        for _ in range(steps):
            result = self.tick()
            if result is None:
                break
            out.append(result)
        return out
