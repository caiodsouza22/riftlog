"""Named hooks that wrap step calls."""

from __future__ import annotations

from collections.abc import Callable

from riftlog.domain.errors import PluginBroken

Hook = Callable[..., object]


class HookChain:
    def __init__(self) -> None:
        self._before: list[Hook] = []
        self._after: list[Hook] = []

    def before(self, fn: Hook) -> Hook:
        self._before.append(fn)
        return fn

    def after(self, fn: Hook) -> Hook:
        self._after.append(fn)
        return fn

    def wrap(self, call: Hook) -> Hook:
        def inner(**kwargs: object) -> object:
            for hook in self._before:
                hook(**kwargs)
            try:
                result = call(**kwargs)
            except Exception as exc:
                raise PluginBroken(getattr(call, "__name__", "call"), str(exc)) from exc
            for hook in self._after:
                hook(result=result, **kwargs)
            return result

        return inner
