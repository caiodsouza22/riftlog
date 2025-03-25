"""Tokens and roles. Bearer string maps to a role."""

from __future__ import annotations

from dataclasses import dataclass

from riftlog.domain.errors import AuthDenied
from riftlog.security.rbac import allowed


@dataclass(frozen=True)
class Token:
    name: str
    role: str


class Gate:
    def __init__(self) -> None:
        self._tokens: dict[str, Token] = {}
        self.required = False

    def issue(self, name: str, role: str = "operator") -> str:
        raw = f"{name}.{role}.{len(self._tokens) + 1}"
        self._tokens[raw] = Token(name, role)
        return raw

    def check(self, raw: str) -> Token:
        if not self.required and not raw:
            return Token("anon", "admin")
        if raw not in self._tokens:
            raise AuthDenied("unknown token")
        return self._tokens[raw]

    def can(self, token: Token, action: str) -> bool:
        return allowed(token.role, action)
