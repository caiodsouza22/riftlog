"""Five-field cron expressions and the next fire time."""

from __future__ import annotations

from datetime import datetime, timedelta

from riftlog.domain.errors import InvalidJob

MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}
DOWS = {
    "sun": 0,
    "mon": 1,
    "tue": 2,
    "wed": 3,
    "thu": 4,
    "fri": 5,
    "sat": 6,
}
BOUNDS = {
    "minute": (0, 59),
    "hour": (0, 23),
    "dom": (1, 31),
    "month": (1, 12),
    "dow": (0, 6),
}


class Agenda:
    def __init__(self, expr: str) -> None:
        parts = expr.strip().split()
        if len(parts) != 5:
            raise InvalidJob("cron needs 5 fields")
        self.expr = expr.strip()
        self.minute = _field(parts[0], "minute")
        self.hour = _field(parts[1], "hour")
        self.dom = _field(parts[2], "dom")
        self.month = _field(parts[3], "month")
        self.dow = _field(parts[4], "dow")

    def matches(self, instant: datetime) -> bool:
        local = instant.replace(second=0, microsecond=0)
        if local.minute not in self.minute:
            return False
        if local.hour not in self.hour:
            return False
        if local.month not in self.month:
            return False
        dow = (local.weekday() + 1) % 7
        dom_star = self.dom == set(range(1, 32))
        dow_star = self.dow == set(range(0, 7))
        if not dom_star and not dow_star:
            return local.day in self.dom or dow in self.dow
        if not dom_star:
            return local.day in self.dom
        if not dow_star:
            return dow in self.dow
        return True

    def next_after(self, instant: datetime, limit: int = 366 * 24 * 60) -> datetime:
        cursor = instant.replace(second=0, microsecond=0) + timedelta(minutes=1)
        for _ in range(limit):
            if self.matches(cursor):
                return cursor
            cursor += timedelta(minutes=1)
        raise InvalidJob(f"cron never fires: {self.expr}")


def _field(raw: str, kind: str) -> set[int]:
    lo, hi = BOUNDS[kind]
    names = MONTHS if kind == "month" else DOWS if kind == "dow" else {}
    values: set[int] = set()
    for chunk in raw.lower().split(","):
        chunk = chunk.strip()
        if not chunk:
            raise InvalidJob("empty cron chunk")
        step = 1
        if "/" in chunk:
            chunk, step_s = chunk.split("/", 1)
            step = int(step_s)
            if step < 1:
                raise InvalidJob("cron step must be >= 1")
        if chunk in {"*", "?"}:
            start, end = lo, hi
        elif "-" in chunk:
            a, b = chunk.split("-", 1)
            start, end = _token(a, names, lo, hi), _token(b, names, lo, hi)
            if start > end:
                raise InvalidJob("cron range is backwards")
        else:
            start = end = _token(chunk, names, lo, hi)
        values.update(range(start, end + 1, step))
    return values


def _token(raw: str, names: dict[str, int], lo: int, hi: int) -> int:
    if raw in names:
        value = names[raw]
    else:
        try:
            value = int(raw)
        except ValueError as exc:
            raise InvalidJob(f"bad cron token: {raw}") from exc
    if value < lo or value > hi:
        raise InvalidJob(f"cron value {value} out of {lo}-{hi}")
    return value
