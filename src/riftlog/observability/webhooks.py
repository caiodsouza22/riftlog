"""In-memory webhook sink used by the notifier."""

from __future__ import annotations

from riftlog.domain.entities import JobRun


class WebhookSink:
    def __init__(self, url: str = "memory://local") -> None:
        self.url = url
        self.emitted: list[JobRun] = []

    def emit(self, run: JobRun) -> None:
        self.emitted.append(run)
