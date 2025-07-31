"""Tenants isolate jobs, secrets, and run lists."""

from __future__ import annotations

from dataclasses import dataclass, field

from riftlog.domain.errors import TenantDenied


@dataclass
class Tenant:
    tenant_id: str
    label: str = ""
    active: bool = True
    quotas: dict[str, float] = field(default_factory=dict)


class Tenants:
    def __init__(self) -> None:
        self._items: dict[str, Tenant] = {}
        self.put(Tenant("default", "default tenant"))

    def put(self, tenant: Tenant) -> Tenant:
        if not tenant.tenant_id:
            raise TenantDenied("", "empty tenant_id")
        self._items[tenant.tenant_id] = tenant
        return tenant

    def get(self, tenant_id: str) -> Tenant:
        if tenant_id not in self._items:
            raise TenantDenied(tenant_id, "not found")
        return self._items[tenant_id]

    def require_active(self, tenant_id: str) -> Tenant:
        tenant = self.get(tenant_id)
        if not tenant.active:
            raise TenantDenied(tenant_id, "disabled")
        return tenant

    def list(self) -> list[Tenant]:
        return [self._items[key] for key in sorted(self._items)]
