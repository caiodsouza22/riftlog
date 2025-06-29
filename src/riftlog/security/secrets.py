"""Local secret map. Values never show up in logs or dump_yaml of a job."""

from __future__ import annotations

from riftlog.domain.errors import SecretMissing


class Vault:
    def __init__(self) -> None:
        self._data: dict[tuple[str, str], str] = {}

    def put(self, name: str, value: str, tenant_id: str = "default") -> None:
        if not name:
            raise SecretMissing("")
        self._data[(tenant_id, name)] = value

    def get(self, name: str, tenant_id: str = "default") -> str:
        key = (tenant_id, name)
        if key not in self._data:
            raise SecretMissing(name)
        return self._data[key]

    def names(self, tenant_id: str = "default") -> list[str]:
        return sorted(name for tenant, name in self._data if tenant == tenant_id)

    def redact(self, text: str, tenant_id: str = "default") -> str:
        out = text
        for (tenant, _name), value in self._data.items():
            if tenant != tenant_id or not value:
                continue
            out = out.replace(value, "***")
        return out
