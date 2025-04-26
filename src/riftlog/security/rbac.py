"""Role names used by the HTTP API."""

from __future__ import annotations

ROLES = {
    "viewer": {"read"},
    "operator": {"read", "run"},
    "admin": {"read", "run", "admin", "secrets"},
}


def allowed(role: str, action: str) -> bool:
    grants = ROLES.get(role, set())
    return action in grants or "admin" in grants


def actions(role: str) -> set[str]:
    return set(ROLES.get(role, set()))
