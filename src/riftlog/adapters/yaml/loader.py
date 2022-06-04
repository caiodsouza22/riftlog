"""Load a JobSpec from the tiny YAML dialect."""

from __future__ import annotations

from pathlib import Path

from riftlog.adapters.yaml.parser import parse_yaml
from riftlog.domain.entities import JobSpec, StepSpec
from riftlog.domain.errors import InvalidJob
from riftlog.domain.graph import validate_needs


def load_job(source: str | Path) -> JobSpec:
    path = Path(source)
    text = path.read_text(encoding="utf-8") if path.exists() and path.is_file() else str(source)
    return parse_job(text)


def parse_job(text: str) -> JobSpec:
    data = parse_yaml(text)
    if not isinstance(data, dict):
        raise InvalidJob("job spec must be a mapping")
    name = str(data.get("name") or "")
    schedule = data.get("schedule")
    schedule_s = None if schedule in (None, "") else str(schedule)
    steps_raw = data.get("steps") if "steps" in data else data.get("tasks")
    steps = _steps(steps_raw)
    job = JobSpec(
        name=name,
        steps=steps,
        schedule=schedule_s,
        timezone=str(data.get("timezone") or "UTC"),
        label=str(data.get("label") or ""),
        tenant_id=str(data.get("tenant") or data.get("tenant_id") or "default"),
        max_parallel=int(data.get("max_parallel") or 0),
    )
    validate_needs(job)
    return job


def _steps(raw: object) -> list[StepSpec]:
    if isinstance(raw, list):
        return [_one_step(item, index) for index, item in enumerate(raw)]
    if isinstance(raw, dict):
        out: list[StepSpec] = []
        for name, body in raw.items():
            if not isinstance(body, dict):
                raise InvalidJob(f"step {name} must be a mapping")
            payload = dict(body)
            payload["name"] = name
            out.append(_one_step(payload, len(out)))
        return out
    raise InvalidJob("steps must be a list or mapping")


_RESERVED = {
    "name",
    "call",
    "run",
    "needs",
    "requires",
    "retries",
    "retry_seconds",
    "timeout_seconds",
    "payload",
    "queue",
    "priority",
    "cpu",
    "memory_mb",
}


def _one_step(item: object, index: int) -> StepSpec:
    if not isinstance(item, dict):
        raise InvalidJob(f"step {index} must be a mapping")
    name = str(item.get("name") or "")
    call = str(item.get("call") or item.get("run") or "")
    needs_raw = item.get("needs") or item.get("requires") or []
    if isinstance(needs_raw, str):
        needs = [needs_raw]
    elif isinstance(needs_raw, list):
        needs = [str(dep) for dep in needs_raw]
    else:
        raise InvalidJob(f"step {name} needs must be a list")
    payload = item.get("payload") if isinstance(item.get("payload"), dict) else {}
    extra = {key: value for key, value in item.items() if key not in _RESERVED}
    merged = {**extra, **payload}
    timeout = item.get("timeout_seconds")
    return StepSpec(
        name=name,
        call=call,
        needs=needs,
        retries=int(item.get("retries") or 0),
        retry_seconds=float(item.get("retry_seconds") or 1.0),
        timeout_seconds=None if timeout in (None, "") else float(timeout),
        payload=merged,
        queue=str(item.get("queue") or "default"),
        priority=int(item.get("priority") or 0),
        cpu=float(item.get("cpu") or 1.0),
        memory_mb=float(item.get("memory_mb") or 64.0),
    )
