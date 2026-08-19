"""Built-in callables registered on import of riftlog.tasks."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from riftlog.application.catalog import task


@task("core.echo")
def echo(message: str = "", **kwargs: object) -> str:
    return str(message)


@task("core.fail")
def fail(reason: str = "failed", **kwargs: object) -> None:
    raise RuntimeError(reason)


@task("core.add")
def add(left: float = 0, right: float = 0, **kwargs: object) -> float:
    return float(left) + float(right)


@task("text.upper")
def text_upper(**kwargs: object) -> str:
    return str(kwargs.get("message", "")).upper()


@task("text.lower")
def text_lower(**kwargs: object) -> str:
    return str(kwargs.get("message", "")).lower()


@task("text.reverse")
def text_reverse(**kwargs: object) -> str:
    return str(kwargs.get("message", ""))[::-1]


@task("text.len")
def text_len(**kwargs: object) -> int:
    return len(str(kwargs.get("message", "")))


@task("text.strip")
def text_strip(**kwargs: object) -> str:
    return str(kwargs.get("message", "")).strip()


@task("text.repeat")
def text_repeat(**kwargs: object) -> str:
    times = int(kwargs.get("times", 1) or 1)
    return str(kwargs.get("message", "")) * max(0, times)


@task("math.mul")
def math_mul(**kwargs: object) -> float:
    return float(kwargs.get("left", 1)) * float(kwargs.get("right", 1))


@task("math.sub")
def math_sub(**kwargs: object) -> float:
    return float(kwargs.get("left", 0)) - float(kwargs.get("right", 0))


@task("math.div")
def math_div(**kwargs: object) -> float:
    right = float(kwargs.get("right", 1))
    if right == 0:
        raise ZeroDivisionError("right is 0")
    return float(kwargs.get("left", 0)) / right


@task("math.min")
def math_min(**kwargs: object) -> float:
    return min(float(kwargs.get("left", 0)), float(kwargs.get("right", 0)))


@task("math.max")
def math_max(**kwargs: object) -> float:
    return max(float(kwargs.get("left", 0)), float(kwargs.get("right", 0)))


@task("math.abs")
def math_abs(**kwargs: object) -> float:
    return abs(float(kwargs.get("value", 0)))


@task("math.mod")
def math_mod(**kwargs: object) -> float:
    right = float(kwargs.get("right", 1))
    if right == 0:
        raise ZeroDivisionError("right is 0")
    return float(kwargs.get("left", 0)) % right


@task("hash.sha256")
def hash_sha256(**kwargs: object) -> str:
    return hashlib.sha256(str(kwargs.get("message", "")).encode()).hexdigest()


@task("hash.md5")
def hash_md5(**kwargs: object) -> str:
    return hashlib.md5(str(kwargs.get("message", "")).encode()).hexdigest()


@task("json.dumps")
def json_dumps(**kwargs: object) -> str:
    return json.dumps(kwargs.get("value", {}), sort_keys=True)


@task("json.loads")
def json_loads(**kwargs: object) -> object:
    raw = kwargs.get("text", "{}")
    return json.loads(str(raw))


@task("fs.touch")
def fs_touch(**kwargs: object) -> str:
    path = str(kwargs.get("path", "riftlog.tmp"))
    Path(path).write_text("", encoding="utf-8")
    return path


@task("time.stamp")
def time_stamp(**kwargs: object) -> str:
    return datetime.now(timezone.utc).isoformat()


@task("bool.and")
def bool_and(**kwargs: object) -> bool:
    return bool(kwargs.get("left")) and bool(kwargs.get("right"))


@task("bool.or")
def bool_or(**kwargs: object) -> bool:
    return bool(kwargs.get("left")) or bool(kwargs.get("right"))


@task("bool.not")
def bool_not(**kwargs: object) -> bool:
    return not bool(kwargs.get("value"))


@task("list.len")
def list_len(**kwargs: object) -> int:
    value = kwargs.get("items") or []
    if not isinstance(value, list):
        return 0
    return len(value)


@task("list.join")
def list_join(**kwargs: object) -> str:
    items = kwargs.get("items") or []
    sep = str(kwargs.get("sep", ","))
    if not isinstance(items, list):
        return ""
    return sep.join(str(item) for item in items)
