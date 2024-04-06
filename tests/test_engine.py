from datetime import datetime, timezone

from riftlog.adapters.time import FrozenClock
from riftlog.application.catalog import Catalog
from riftlog.application.engine import Engine
from riftlog.adapters.yaml import parse_job
from riftlog.domain.states import RunState, StepState


def test_linear_ok():
    job = parse_job(
        """
name: ping
steps:
  ping:
    call: core.echo
    message: pong
"""
    )
    run = Engine().run(job)
    assert run.state == RunState.OK
    assert run.results["ping"].output == "pong"


def test_needs_order():
    seen: list[str] = []
    cat = Catalog()

    @cat.task("t.mark")
    def mark(tag: str = "", **kwargs: object) -> str:
        seen.append(tag)
        return tag

    job = parse_job(
        """
name: chain
steps:
  first:
    call: t.mark
    tag: a
  second:
    call: t.mark
    tag: b
    needs: [first]
"""
    )
    run = Engine(cat).run(job)
    assert run.state == RunState.OK
    assert seen == ["a", "b"]


def test_retry_then_ok():
    hits = {"n": 0}
    cat = Catalog()

    @cat.task("t.flaky")
    def flaky(**kwargs: object) -> str:
        hits["n"] += 1
        if hits["n"] < 3:
            raise RuntimeError("nope")
        return "ok"

    job = parse_job(
        """
name: flaky
steps:
  job:
    call: t.flaky
    retries: 5
    retry_seconds: 0
"""
    )
    clock = FrozenClock(datetime(2024, 1, 1, tzinfo=timezone.utc))
    run = Engine(cat, clock).run(job)
    assert run.state == RunState.OK
    assert run.results["job"].attempts == 3


def test_fail_skips_downstream():
    job = parse_job(
        """
name: boom
steps:
  bad:
    call: core.fail
    reason: nope
  later:
    call: core.echo
    message: x
    needs: [bad]
"""
    )
    run = Engine().run(job)
    assert run.state == RunState.FAILED
    assert run.results["bad"].state == StepState.FAILED
    assert run.results["later"].state == StepState.SKIPPED


def test_omit_label_and_tenant():
    job = parse_job(
        """
name: t
steps:
  p:
    call: core.echo
    message: x
"""
    )
    assert job.label == ""
    assert job.tenant_id == "default"


def test_max_parallel_caps_ready_batch():
    cat = Catalog()
    seen: list[str] = []

    @cat.task("t.mark")
    def mark(tag: str = "", **kwargs: object) -> str:
        seen.append(tag)
        return tag

    job = parse_job(
        """
name: wave
max_parallel: 1
steps:
  a:
    call: t.mark
    tag: a
  b:
    call: t.mark
    tag: b
  c:
    call: t.mark
    tag: c
    needs: [a, b]
"""
    )
    run = Engine(cat).run(job)
    assert run.state == RunState.OK
    assert seen[:2] == ["a", "b"]
    assert seen[-1] == "c"


def test_tasks_alias_accepted():
    job = parse_job(
        """
name: alias
tasks:
  ping:
    call: core.echo
    message: z
"""
    )
    assert job.steps[0].name == "ping"
