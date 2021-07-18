"""Lifecycle enums for steps and job runs."""

from __future__ import annotations

from enum import Enum


class StepState(str, Enum):
    PENDING = "pending"
    READY = "ready"
    RUNNING = "running"
    OK = "ok"
    FAILED = "failed"
    SKIPPED = "skipped"


class RunState(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    OK = "ok"
    FAILED = "failed"
    CANCELLED = "cancelled"


class TriggerKind(str, Enum):
    MANUAL = "manual"
    AGENDA = "agenda"
    HOOK = "hook"
    REPLAY = "replay"
