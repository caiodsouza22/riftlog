"""Named queues of pending step work."""

from __future__ import annotations

from dataclasses import dataclass

from riftlog.domain.entities import StepSpec
from riftlog.workers.priority import PriorityQueue


@dataclass
class Work:
    run_id: str
    job: str
    step: StepSpec
    tenant_id: str = "default"


class Dispatch:
    def __init__(self) -> None:
        self._queues: dict[str, PriorityQueue] = {}

    def queue(self, name: str) -> PriorityQueue:
        if name not in self._queues:
            self._queues[name] = PriorityQueue()
        return self._queues[name]

    def submit(self, work: Work) -> None:
        self.queue(work.step.queue).push(work, work.step.priority)

    def take(self, name: str = "default") -> Work | None:
        bucket = self.queue(name)
        if bucket.empty():
            return None
        payload = bucket.pop()
        assert isinstance(payload, Work)
        return payload

    def names(self) -> list[str]:
        return sorted(self._queues)

    def pending(self, name: str = "default") -> int:
        return len(self.queue(name))
