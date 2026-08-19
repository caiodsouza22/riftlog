from datetime import datetime, timezone

import pytest

from riftlog.adapters.time import FrozenClock
from riftlog.adapters.yaml import parse_job
from riftlog.api import JobApi
from riftlog.application.catalog import GLOBAL, Catalog
from riftlog.application.config import load_config
from riftlog.application.diagnose import diagnose
from riftlog.application.engine import Engine
from riftlog.application.export import run_to_dict, run_to_json
from riftlog.application.generate import generate, generate_job
from riftlog.application.hooks import HookChain
from riftlog.application.pipeline import Pipeline
from riftlog.application.retry import RetryPlan, should_retry
from riftlog.application.scheduler import Scheduler
from riftlog.application.validate import validate_job
from riftlog.cron.windows import catchup_minutes, in_quiet_hours, minute_bucket
from riftlog.domain.errors import AuthDenied, CapExceeded, PluginBroken, SecretMissing, TenantDenied
from riftlog.domain.states import RunState
from riftlog.observability import AuditLog, Fanout, Metrics, WebhookSink, health
from riftlog.security import Caps, Gate, Tenants, Vault
from riftlog.security.tenants import Tenant
from riftlog.workers import Dispatch, Work, Worker


def test_retry_plan_delay():
    plan = RetryPlan(3, 2.0)
    assert plan.delay() == 0.0
    assert plan.record_fail()
    assert plan.delay() == 2.0
    assert plan.record_fail()
    assert plan.delay() == 4.0
    assert should_retry(1, 2)


def test_pipeline_load_and_run():
    pipe = Pipeline()
    spec = pipe.load(
        "name: ping\nsteps:\n  ping:\n    call: core.echo\n    message: hi\n"
    )
    run = pipe.run(spec.name)
    assert run.state == RunState.OK
    assert pipe.get(run.run_id).run_id == run.run_id


def test_scheduler_fires_once_per_minute():
    clock = FrozenClock(datetime(2024, 1, 1, 2, 30, tzinfo=timezone.utc))
    job = parse_job(
        "name: backup\nschedule: 30 2 * * *\nsteps:\n  dump:\n    call: core.echo\n    message: dump\n"
    )
    sched = Scheduler(clock=clock)
    sched.add(job)
    first = sched.tick()
    second = sched.tick()
    assert len(first) == 1
    assert second == []


def test_worker_drains_queue():
    dispatch = Dispatch()
    job = parse_job("name: p\nsteps:\n  ping:\n    call: core.echo\n    message: z\n")
    dispatch.submit(Work("r1", "p", job.steps[0]))
    worker = Worker(dispatch)
    out = worker.drain()
    assert len(out) == 1
    assert out[0].output == "z"


def test_gate_and_rbac():
    gate = Gate()
    gate.required = True
    raw = gate.issue("caio", "viewer")
    token = gate.check(raw)
    assert token.role == "viewer"
    assert gate.can(token, "read")
    assert not gate.can(token, "run")
    with pytest.raises(AuthDenied):
        gate.check("nope")


def test_vault_redact():
    vault = Vault()
    vault.put("token", "secret-value")
    assert vault.get("token") == "secret-value"
    assert "***" in vault.redact("using secret-value here")
    with pytest.raises(SecretMissing):
        vault.get("missing")


def test_tenants_disabled():
    book = Tenants()
    book.put(Tenant("acme", active=False))
    with pytest.raises(TenantDenied):
        book.require_active("acme")


def test_caps_hold_and_release():
    caps = Caps()
    caps.cap("default", cpu=1.0, memory_mb=64.0)
    job = parse_job("name: p\nsteps:\n  ping:\n    call: core.echo\n    message: z\n")
    caps.hold(job)
    with pytest.raises(CapExceeded):
        caps.hold(job)
    caps.release(job)
    caps.hold(job)


def test_api_health_and_post():
    api = JobApi()
    code, body = api.handle("GET", "/health", "")
    assert code == 200
    code, body = api.handle(
        "POST",
        "/runs",
        '{"yaml": "name: ping\\nsteps:\\n  ping:\\n    call: core.echo\\n    message: hi\\n"}',
    )
    assert code == 201
    assert body["state"] == "ok"
    code, listed = api.handle("GET", "/runs?job=ping", "")
    assert listed["runs"]


def test_api_forbidden_when_viewer():
    gate = Gate()
    gate.required = True
    token = gate.issue("v", "viewer")
    api = JobApi(gate=gate)
    code, _ = api.handle("POST", "/runs", '{"job": "x"}', token)
    assert code == 403


def test_diagnose_clean_and_failed():
    ok = Engine().run(parse_job("name: p\nsteps:\n  ping:\n    call: core.echo\n    message: z\n"))
    assert diagnose(ok) == ["run finished clean"]
    bad = Engine().run(parse_job("name: b\nsteps:\n  bad:\n    call: core.fail\n    reason: timeout boom\n"))
    notes = diagnose(bad)
    assert any("timeout" in line for line in notes)


def test_generate_templates():
    assert "dump" in generate("backup nightly")
    job = generate_job("etl please")
    assert job.name == "etl"


def test_export_and_metrics():
    run = Engine().run(parse_job("name: p\nsteps:\n  ping:\n    call: core.echo\n    message: z\n"))
    blob = run_to_dict(run)
    assert blob["job"] == "p"
    assert "run_id" in run_to_json(run)
    metrics = Metrics()
    metrics.record_run("p", True, 1, 0)
    assert metrics.snapshot()["ok"] == 1


def test_audit_and_fanout():
    sink = WebhookSink()
    fan = Fanout(hooks=[sink], clock=FrozenClock(datetime(2024, 1, 1, tzinfo=timezone.utc)))
    run = Engine().run(parse_job("name: p\nsteps:\n  ping:\n    call: core.echo\n    message: z\n"))
    fan.send(run)
    assert sink.emitted[0].run_id == run.run_id
    log = AuditLog()
    log.record(datetime(2024, 1, 1, tzinfo=timezone.utc), "caio", "run", "r1")
    assert log.list()[0].actor == "caio"


def test_health_payload():
    payload = health()
    assert payload["ok"] is True


def test_quiet_hours_and_catchup():
    now = datetime(2024, 1, 1, 3, 10, tzinfo=timezone.utc)
    assert in_quiet_hours(now, 2, 5)
    assert not in_quiet_hours(now, 8, 10)
    last = datetime(2024, 1, 1, 3, 8, tzinfo=timezone.utc)
    mins = catchup_minutes(last, now)
    assert minute_bucket(mins[0]).minute == 9


def test_config_defaults_and_file(tmp_path):
    assert load_config().http_port == 8080
    path = tmp_path / "cfg.yaml"
    path.write_text("http_port: 9090\nrequire_auth: true\n", encoding="utf-8")
    cfg = load_config(path)
    assert cfg.http_port == 9090
    assert cfg.require_auth is True


def test_hooks_wrap_and_plugin_error():
    chain = HookChain()
    seen: list[str] = []

    @chain.before
    def before(**kwargs: object) -> None:
        seen.append("b")

    def boom(**kwargs: object) -> None:
        raise RuntimeError("x")

    wrapped = chain.wrap(boom)
    with pytest.raises(PluginBroken):
        wrapped(message="z")
    assert seen == ["b"]


def test_validate_job_schedule():
    job = parse_job(
        "name: n\nschedule: 0 * * * *\nsteps:\n  p:\n    call: core.echo\n    message: z\n"
    )
    validate_job(job)


def test_catalog_unknown():
    with pytest.raises(Exception):
        GLOBAL.get("no.such.call")


def test_core_math_and_text():
    assert GLOBAL.get("core.add")(left=2, right=3) == 5
    assert GLOBAL.get("text.upper")(message="ab") == "AB"
    assert GLOBAL.get("math.mul")(left=2, right=4) == 8.0
