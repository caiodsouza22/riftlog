from datetime import datetime, timezone

from riftlog.adapters.time import FrozenClock
from riftlog.domain.states import RunState
from riftlog.adapters.yaml import parse_job
from riftlog.adapters.persistence import MemoryStore, SqliteStore
from riftlog.application.engine import Engine
from riftlog.domain.errors import RunMissing
import pytest


YAML = """
name: ping
steps:
  ping:
    call: core.echo
    message: hi
"""


def test_memory_roundtrip():
    run = Engine().run(parse_job(YAML))
    store = MemoryStore()
    store.put(run)
    got = store.get(run.run_id)
    assert got.job == "ping"
    assert store.list("ping")[0].run_id == run.run_id


def test_sqlite_roundtrip(tmp_path):
    run = Engine().run(parse_job(YAML))
    store = SqliteStore(tmp_path / "runs.db")
    store.put(run)
    got = store.get(run.run_id)
    assert got.state == RunState.OK
    assert got.results["ping"].output == "hi"
    assert store.list(tenant_id="default")[0].run_id == run.run_id


def test_frozen_clock_stamps():
    clock = FrozenClock(datetime(2024, 6, 1, 12, 0, tzinfo=timezone.utc))
    run = Engine(clock=clock).run(parse_job(YAML))
    assert run.created_at == clock.now()


def test_memory_missing():
    with pytest.raises(RunMissing):
        MemoryStore().get("nope")


def test_list_filters_job_and_tenant():
    store = MemoryStore()
    a = Engine().run(parse_job("name: a\nsteps:\n  p:\n    call: core.echo\n    message: x\n"))
    b = Engine().run(parse_job("name: b\ntenant: other\nsteps:\n  p:\n    call: core.echo\n    message: y\n"))
    store.put(a)
    store.put(b)
    assert [row.job for row in store.list(job="a")] == ["a"]
    assert [row.tenant_id for row in store.list(tenant_id="other")] == ["other"]
