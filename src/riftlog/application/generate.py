"""Turn a short wish into a YAML job. Templates only, no remote model."""

from __future__ import annotations

from riftlog.adapters.yaml.loader import parse_job
from riftlog.adapters.yaml.parser import dump_yaml

TEMPLATES = {
    "backup": {
        "name": "backup",
        "schedule": "30 2 * * *",
        "steps": {
            "dump": {"call": "core.echo", "message": "dump"},
            "upload": {"call": "core.echo", "message": "upload", "needs": ["dump"]},
        },
    },
    "etl": {
        "name": "etl",
        "steps": {
            "extract": {"call": "core.echo", "message": "extract"},
            "transform": {"call": "core.add", "left": 1, "right": 2, "needs": ["extract"]},
            "load": {"call": "core.echo", "message": "load", "needs": ["transform"]},
        },
    },
    "ping": {
        "name": "ping",
        "steps": {"ping": {"call": "core.echo", "message": "pong"}},
    },
}


def generate(wish: str) -> str:
    key = _pick(wish)
    return dump_yaml(TEMPLATES[key])


def generate_job(wish: str):
    return parse_job(generate(wish))


def _pick(wish: str) -> str:
    text = wish.lower()
    if "backup" in text or "dump" in text:
        return "backup"
    if "etl" in text or "extract" in text:
        return "etl"
    return "ping"
