import pytest

from riftlog.adapters.time import FrozenClock
from riftlog.domain.entities import JobSpec, StepSpec
from riftlog.domain.errors import InvalidJob
from datetime import datetime, timezone


def test_step_rejects_empty_name():
    with pytest.raises(ValueError):
        StepSpec(name="", call="core.echo")


def test_step_rejects_empty_call():
    with pytest.raises(ValueError):
        StepSpec(name="a", call="")


def test_step_rejects_negative_retries():
    with pytest.raises(ValueError):
        StepSpec(name="a", call="core.echo", retries=-1)


def test_step_rejects_negative_retry_seconds():
    with pytest.raises(ValueError):
        StepSpec(name="a", call="core.echo", retry_seconds=-0.1)


def test_step_rejects_non_positive_timeout():
    with pytest.raises(ValueError):
        StepSpec(name="a", call="core.echo", timeout_seconds=0)


def test_step_rejects_non_positive_cpu():
    with pytest.raises(ValueError):
        StepSpec(name="a", call="core.echo", cpu=0)


def test_job_rejects_empty_name():
    with pytest.raises(ValueError):
        JobSpec(name="", steps=[StepSpec(name="a", call="core.echo")])


def test_job_rejects_no_steps():
    with pytest.raises(ValueError):
        JobSpec(name="j", steps=[])


def test_job_rejects_duplicate_names():
    with pytest.raises(ValueError):
        JobSpec(
            name="j",
            steps=[
                StepSpec(name="a", call="core.echo"),
                StepSpec(name="a", call="core.add"),
            ],
        )


def test_frozen_clock_rejects_naive():
    with pytest.raises(ValueError):
        FrozenClock(datetime(2024, 1, 1))


def test_frozen_clock_set_rejects_naive():
    clock = FrozenClock(datetime(2024, 1, 1, tzinfo=timezone.utc))
    with pytest.raises(ValueError):
        clock.set(datetime(2024, 1, 2))


def test_frozen_clock_advance():
    clock = FrozenClock(datetime(2024, 1, 1, tzinfo=timezone.utc))
    clock.advance(60)
    assert clock.now().minute == 1
