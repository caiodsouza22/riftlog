"""Counters and timings for a process. No network."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Metrics:
    runs: int = 0
    ok: int = 0
    failed: int = 0
    steps: int = 0
    retries: int = 0
    by_job: dict[str, int] = field(default_factory=dict)

    def record_run(self, job: str, ok: bool, steps: int, retries: int = 0) -> None:
        self.runs += 1
        self.steps += steps
        self.retries += retries
        if ok:
            self.ok += 1
        else:
            self.failed += 1
        self.by_job[job] = self.by_job.get(job, 0) + 1

    def snapshot(self) -> dict[str, object]:
        return {
            "runs": self.runs,
            "ok": self.ok,
            "failed": self.failed,
            "steps": self.steps,
            "retries": self.retries,
            "by_job": dict(self.by_job),
        }
