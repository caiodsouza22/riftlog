"""Typed errors for job specs, runs, and workers."""

from __future__ import annotations


class JobError(Exception):
    """Base error for the local job runner."""


class InvalidJob(JobError):
    def __init__(self, message: str = "invalid job spec") -> None:
        super().__init__(message)


class UnknownStep(JobError):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"unknown step: {name}")


class CycleInGraph(JobError):
    def __init__(self, nodes: list[str]) -> None:
        self.nodes = list(nodes)
        super().__init__("cycle in step graph: " + " -> ".join(nodes))


class RunMissing(JobError):
    def __init__(self, run_id: str) -> None:
        self.run_id = run_id
        super().__init__(f"run not found: {run_id}")


class StepFailed(JobError):
    def __init__(self, step: str, reason: str) -> None:
        self.step = step
        self.reason = reason
        super().__init__(f"step {step} failed: {reason}")


class RetryGone(StepFailed):
    def __init__(self, step: str, attempts: int, reason: str) -> None:
        self.attempts = attempts
        super().__init__(step, f"retries exhausted after {attempts}: {reason}")


class AuthDenied(JobError):
    def __init__(self, message: str = "not authorized") -> None:
        super().__init__(message)


class TenantDenied(JobError):
    def __init__(self, tenant_id: str, message: str = "tenant error") -> None:
        self.tenant_id = tenant_id
        super().__init__(f"{tenant_id}: {message}")


class CapExceeded(JobError):
    def __init__(self, resource: str, used: float, cap: float) -> None:
        self.resource = resource
        self.used = used
        self.cap = cap
        super().__init__(f"{resource} limit exceeded ({used} > {cap})")


class SecretMissing(JobError):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"secret not found: {name}")


class PluginBroken(JobError):
    def __init__(self, plugin: str, message: str) -> None:
        self.plugin = plugin
        super().__init__(f"plugin {plugin}: {message}")


class QueueEmpty(JobError):
    def __init__(self, queue: str = "default") -> None:
        self.queue = queue
        super().__init__(f"queue empty: {queue}")


class AgendaMiss(JobError):
    def __init__(self, expr: str) -> None:
        self.expr = expr
        super().__init__(f"cron never fires: {expr}")
