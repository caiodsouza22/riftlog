"""Persistence port for job runs."""

from __future__ import annotations

from typing import Protocol

from riftlog.domain.entities import JobRun


class RunStore(Protocol):
    def put(self, run: JobRun) -> JobRun: ...

    def get(self, run_id: str) -> JobRun: ...

    def list(self, job: str | None = None, tenant_id: str | None = None) -> list[JobRun]: ...
