"""Fan-out after a run finishes."""

from __future__ import annotations

from riftlog.adapters.time.clocks import WallClock
from riftlog.domain.entities import JobRun
from riftlog.observability.audit import AuditLog
from riftlog.observability.webhooks import WebhookSink
from riftlog.ports.clock import Clock
from riftlog.ports.notifier import Notifier as NotifierPort


class Fanout:
    def __init__(
        self,
        hooks: list[WebhookSink] | None = None,
        audit: AuditLog | None = None,
        clock: Clock | None = None,
        actor: str = "system",
    ) -> None:
        self.hooks = hooks or []
        self.audit = audit or AuditLog()
        self.clock = clock or WallClock()
        self.actor = actor

    def send(self, run: JobRun) -> None:
        self.audit.record(
            self.clock.now(),
            self.actor,
            "run.finished",
            run.run_id,
            run.tenant_id,
            run.state.value,
        )
        for hook in self.hooks:
            hook.emit(run)


def as_notifier(fanout: Fanout) -> NotifierPort:
    return fanout
