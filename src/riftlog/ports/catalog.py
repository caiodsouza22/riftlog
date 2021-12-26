"""Port for named callables used by step `call` fields."""

from __future__ import annotations

from collections.abc import Callable
from typing import Protocol

Call = Callable[..., object]


class CatalogPort(Protocol):
    def register(self, name: str, fn: Call) -> Call: ...

    def get(self, name: str) -> Call: ...

    def names(self) -> list[str]: ...
