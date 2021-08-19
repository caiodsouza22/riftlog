"""Domain records: steps, jobs, and run snapshots. No I/O here."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from riftlog.domain.states import RunState, StepState, TriggerKind


@dataclass
class StepSpec:
    name: str
    call: str
    needs: list[str] = field(default_factory=list)
    retries: int = 0
    retry_seconds: float = 1.0
    timeout_seconds: float | None = None
    payload: dict[str, object] = field(default_factory=dict)
    queue: str = "default"
    priority: int = 0
    cpu: float = 1.0
    memory_mb: float = 64.0

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("step name is empty")
        if not self.call:
            raise ValueError("step call is empty")
        if self.retries < 0:
            raise ValueError("retries must be >= 0")
        if self.retry_seconds < 0:
            raise ValueError("retry_seconds must be >= 0")
        if self.timeout_seconds is not None and self.timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive")
        if self.cpu <= 0:
            raise ValueError("cpu must be positive")
        if self.memory_mb <= 0:
            raise ValueError("memory_mb must be positive")


@dataclass
class JobSpec:
    name: str
    steps: list[StepSpec]
    schedule: str | None = None
    timezone: str = "UTC"
    label: str = ""
    tenant_id: str = "default"
    max_parallel: int = 0

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("job name is empty")
        if not self.steps:
            raise ValueError("job has no steps")
        names = [step.name for step in self.steps]
        if len(names) != len(set(names)):
            raise ValueError("duplicate step names")
        if self.max_parallel < 0:
            raise ValueError("max_parallel must be >= 0")

    def by_name(self) -> dict[str, StepSpec]:
        return {step.name: step for step in self.steps}

    def step_names(self) -> list[str]:
        return [step.name for step in self.steps]


@dataclass
class StepResult:
    name: str
    state: StepState
    attempts: int = 0
    output: object = None
    error: str = ""
    started_at: datetime | None = None
    finished_at: datetime | None = None
    log_lines: list[str] = field(default_factory=list)


@dataclass
class JobRun:
    run_id: str
    job: str
    state: RunState
    created_at: datetime
    tenant_id: str = "default"
    started_at: datetime | None = None
    finished_at: datetime | None = None
    results: dict[str, StepResult] = field(default_factory=dict)
    trigger: str = TriggerKind.MANUAL.value
    label: str = ""

    def result_of(self, name: str) -> StepResult:
        if name not in self.results:
            raise KeyError(name)
        return self.results[name]

    def ok_names(self) -> list[str]:
        return [name for name, row in self.results.items() if row.state == StepState.OK]

    def failed_names(self) -> list[str]:
        return [name for name, row in self.results.items() if row.state == StepState.FAILED]
