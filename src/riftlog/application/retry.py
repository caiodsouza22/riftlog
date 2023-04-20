"""Retry budget: attempts and delay from the previous next, not from now."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RetryPlan:
    retries: int
    retry_seconds: float
    attempts: int = 0

    def remaining(self) -> int:
        return max(0, self.retries - self.attempts)

    def record_fail(self) -> bool:
        self.attempts += 1
        return self.attempts <= self.retries

    def delay(self) -> float:
        if self.attempts <= 0:
            return 0.0
        return self.retry_seconds * (2 ** (self.attempts - 1))


def should_retry(attempts: int, retries: int) -> bool:
    return attempts <= retries
