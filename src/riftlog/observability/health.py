"""Liveness payload used by the HTTP /health route and the CLI."""

from __future__ import annotations

from riftlog.adapters.persistence.memory import MemoryStore


def health(store: MemoryStore | None = None) -> dict[str, object]:
    store = store or MemoryStore()
    rows = store.list()
    failed = sum(1 for row in rows if row.state.value == "failed")
    return {"ok": True, "runs": len(rows), "failed": failed}
