"""Soft caps on cpu/memory tokens a tenant may hold at once."""

from __future__ import annotations

from riftlog.domain.entities import JobSpec
from riftlog.domain.errors import CapExceeded


class Caps:
    def __init__(self) -> None:
        self._cpu: dict[str, float] = {}
        self._mem: dict[str, float] = {}
        self._cap_cpu: dict[str, float] = {}
        self._cap_mem: dict[str, float] = {}

    def cap(self, tenant_id: str, cpu: float, memory_mb: float) -> None:
        self._cap_cpu[tenant_id] = cpu
        self._cap_mem[tenant_id] = memory_mb

    def check(self, job: JobSpec) -> None:
        cpu = sum(step.cpu for step in job.steps)
        mem = sum(step.memory_mb for step in job.steps)
        used_cpu = self._cpu.get(job.tenant_id, 0.0) + cpu
        used_mem = self._mem.get(job.tenant_id, 0.0) + mem
        cap_cpu = self._cap_cpu.get(job.tenant_id)
        cap_mem = self._cap_mem.get(job.tenant_id)
        if cap_cpu is not None and used_cpu > cap_cpu:
            raise CapExceeded("cpu", used_cpu, cap_cpu)
        if cap_mem is not None and used_mem > cap_mem:
            raise CapExceeded("memory_mb", used_mem, cap_mem)

    def hold(self, job: JobSpec) -> None:
        self.check(job)
        self._cpu[job.tenant_id] = self._cpu.get(job.tenant_id, 0.0) + sum(
            step.cpu for step in job.steps
        )
        self._mem[job.tenant_id] = self._mem.get(job.tenant_id, 0.0) + sum(
            step.memory_mb for step in job.steps
        )

    def release(self, job: JobSpec) -> None:
        self._cpu[job.tenant_id] = max(
            0.0, self._cpu.get(job.tenant_id, 0.0) - sum(step.cpu for step in job.steps)
        )
        self._mem[job.tenant_id] = max(
            0.0,
            self._mem.get(job.tenant_id, 0.0) - sum(step.memory_mb for step in job.steps),
        )
