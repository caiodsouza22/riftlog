"""Clock adapters. Domain only sees the Clock protocol."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone


class WallClock:
    def now(self) -> datetime:
        return datetime.now(timezone.utc)


class FrozenClock:
    def __init__(self, instant: datetime) -> None:
        if instant.tzinfo is None:
            raise ValueError("FrozenClock needs an aware datetime")
        self._instant = instant

    def now(self) -> datetime:
        return self._instant

    def set(self, instant: datetime) -> None:
        if instant.tzinfo is None:
            raise ValueError("set needs an aware datetime")
        self._instant = instant

    def advance(self, seconds: float) -> datetime:
        self._instant = self._instant + timedelta(seconds=seconds)
        return self._instant
