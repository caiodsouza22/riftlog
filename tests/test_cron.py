from datetime import datetime, timezone

from riftlog.cron import Agenda
from riftlog.domain.errors import InvalidJob
import pytest


def utc(*args: int) -> datetime:
    return datetime(*args, tzinfo=timezone.utc)


def test_hourly():
    cron = Agenda("0 * * * *")
    assert cron.matches(utc(2024, 1, 1, 5, 0))
    assert not cron.matches(utc(2024, 1, 1, 5, 1))


def test_next_after_skips_current_minute():
    cron = Agenda("0 * * * *")
    nxt = cron.next_after(utc(2024, 1, 1, 5, 0))
    assert nxt == utc(2024, 1, 1, 6, 0)


def test_dow_monday():
    cron = Agenda("0 9 * * 1")
    monday = utc(2024, 1, 1, 9, 0)
    assert monday.weekday() == 0
    assert cron.matches(monday)
    assert not cron.matches(utc(2024, 1, 2, 9, 0))


def test_dom_or_dow():
    cron = Agenda("0 0 1 * 1")
    assert cron.matches(utc(2024, 1, 1, 0, 0))


def test_names():
    cron = Agenda("0 0 1 jan mon")
    assert 1 in cron.month
    assert 1 in cron.dow


def test_step():
    cron = Agenda("*/15 * * * *")
    assert cron.matches(utc(2024, 1, 1, 0, 0))
    assert cron.matches(utc(2024, 1, 1, 0, 15))
    assert not cron.matches(utc(2024, 1, 1, 0, 7))


def test_bad_field_count():
    with pytest.raises(InvalidJob):
        Agenda("* * *")


def test_range_backwards():
    with pytest.raises(InvalidJob):
        Agenda("5-1 * * * *")


def test_comma_list():
    cron = Agenda("0,30 * * * *")
    assert cron.matches(utc(2024, 1, 1, 0, 0))
    assert cron.matches(utc(2024, 1, 1, 0, 30))
    assert not cron.matches(utc(2024, 1, 1, 0, 15))
