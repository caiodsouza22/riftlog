"""Notification port used after a run finishes."""

from __future__ import annotations

from typing import Protocol

from riftlog.domain.entities import JobRun


class Notifier(Protocol):
    def send(self, run: JobRun) -> None: ...
