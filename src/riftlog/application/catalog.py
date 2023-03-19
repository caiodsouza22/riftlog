"""Named Python callables used by step `call` fields."""

from __future__ import annotations

from collections.abc import Callable

from riftlog.domain.errors import UnknownStep
from riftlog.ports.catalog import Call


class Catalog:
    def __init__(self) -> None:
        self._calls: dict[str, Call] = {}

    def register(self, name: str, fn: Call) -> Call:
        if not name:
            raise ValueError("call name is empty")
        self._calls[name] = fn
        return fn

    def task(self, name: str) -> Callable[[Call], Call]:
        def wrap(fn: Call) -> Call:
            return self.register(name, fn)

        return wrap

    def get(self, name: str) -> Call:
        if name not in self._calls:
            raise UnknownStep(name)
        return self._calls[name]

    def names(self) -> list[str]:
        return sorted(self._calls)

    def copy(self) -> Catalog:
        other = Catalog()
        other._calls = dict(self._calls)
        return other

    def has(self, name: str) -> bool:
        return name in self._calls


GLOBAL = Catalog()


def task(name: str) -> Callable[[Call], Call]:
    return GLOBAL.task(name)


def register(name: str, fn: Call) -> Call:
    return GLOBAL.register(name, fn)


def get_call(name: str) -> Call:
    return GLOBAL.get(name)
