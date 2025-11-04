"""Append-only audit rows for who kicked a run."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuditEvent:
    at: datetime
    actor: str
    action: str
    target: str
    tenant_id: str = "default"
    detail: str = ""


class AuditLog:
    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def record(
        self,
        at: datetime,
        actor: str,
        action: str,
        target: str,
        tenant_id: str = "default",
        detail: str = "",
    ) -> AuditEvent:
        event = AuditEvent(at, actor, action, target, tenant_id, detail)
        self._events.append(event)
        return event

    def list(self, tenant_id: str | None = None) -> list[AuditEvent]:
        rows = list(self._events)
        if tenant_id:
            rows = [row for row in rows if row.tenant_id == tenant_id]
        return rows
