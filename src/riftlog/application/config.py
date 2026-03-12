"""Load a small json/yaml config for the CLI and the HTTP server."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from riftlog.adapters.yaml.parser import parse_yaml


@dataclass
class AppConfig:
    db_path: str = ":memory:"
    http_host: str = "127.0.0.1"
    http_port: int = 8080
    default_tenant: str = "default"
    require_auth: bool = False


def load_config(path: str | Path | None = None) -> AppConfig:
    if path is None:
        return AppConfig()
    text = Path(path).read_text(encoding="utf-8")
    data = parse_yaml(text)
    if not isinstance(data, dict):
        return AppConfig()
    return AppConfig(
        db_path=str(data.get("db_path") or ":memory:"),
        http_host=str(data.get("http_host") or "127.0.0.1"),
        http_port=int(data.get("http_port") or 8080),
        default_tenant=str(data.get("default_tenant") or "default"),
        require_auth=bool(data.get("require_auth") or False),
    )
