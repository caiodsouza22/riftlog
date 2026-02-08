"""Clock windows used by cron catch-up and quiet hours."""

from __future__ import annotations

from datetime import datetime, timedelta


def minute_bucket(instant: datetime) -> datetime:
    return instant.replace(second=0, microsecond=0)


def in_quiet_hours(instant: datetime, start_hour: int, end_hour: int) -> bool:
    hour = instant.hour
    if start_hour == end_hour:
        return False
    if start_hour < end_hour:
        return start_hour <= hour < end_hour
    return hour >= start_hour or hour < end_hour


def catchup_minutes(last: datetime, now: datetime, cap: int = 24 * 60) -> list[datetime]:
    cursor = minute_bucket(last) + timedelta(minutes=1)
    end = minute_bucket(now)
    out: list[datetime] = []
    while cursor <= end and len(out) < cap:
        out.append(cursor)
        cursor += timedelta(minutes=1)
    return out


def hour_bucket(instant: datetime) -> datetime:
    return instant.replace(minute=0, second=0, microsecond=0)


def same_minute(left: datetime, right: datetime) -> bool:
    return minute_bucket(left) == minute_bucket(right)
