"""Extra checks on a job before it is armed."""

from __future__ import annotations

from riftlog.cron.expr import Agenda
from riftlog.domain.errors import InvalidJob
from riftlog.domain.graph import validate_needs
from riftlog.domain.entities import JobSpec


def validate_job(job: JobSpec) -> None:
    validate_needs(job)
    if job.schedule:
        Agenda(job.schedule)
    if job.max_parallel < 0:
        raise InvalidJob("max_parallel must be >= 0")
    for step in job.steps:
        if step.cpu <= 0 or step.memory_mb <= 0:
            raise InvalidJob(f"{step.name} resource must be positive")
