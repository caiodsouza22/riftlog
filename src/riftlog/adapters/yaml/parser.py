"""Tiny YAML subset: maps, lists, scalars. No tags, no anchors."""

from __future__ import annotations

from riftlog.domain.errors import InvalidJob


def parse_yaml(text: str) -> object:
    lines = _prep(text)
    if not lines:
        return {}
    value, index = _parse_block(lines, 0, 0)
    if index != len(lines):
        raise InvalidJob("yaml trailing content")
    return value


def dump_yaml(value: object, indent: int = 0) -> str:
    return "\n".join(_dump(value, indent)) + "\n"


def _prep(text: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    for raw in text.splitlines():
        if "\t" in raw:
            raise InvalidJob("yaml tabs are not allowed")
        stripped = raw.split("#", 1)[0].rstrip()
        if not stripped:
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        if indent % 2 != 0:
            raise InvalidJob("yaml indent must be multiples of 2")
        rows.append((indent, stripped.lstrip(" ")))
    return rows


def _parse_block(lines: list[tuple[int, str]], index: int, indent: int) -> tuple[object, int]:
    if index >= len(lines):
        return {}, index
    level, body = lines[index]
    if level < indent:
        return {}, index
    if body.startswith("- "):
        return _parse_list(lines, index, level)
    return _parse_map(lines, index, level)


def _parse_map(lines: list[tuple[int, str]], index: int, indent: int) -> tuple[dict[str, object], int]:
    data: dict[str, object] = {}
    while index < len(lines):
        level, body = lines[index]
        if level < indent:
            break
        if level > indent:
            raise InvalidJob("yaml indent jumped")
        if body.startswith("- "):
            raise InvalidJob("yaml list item where a key was expected")
        if ":" not in body:
            raise InvalidJob(f"yaml expected key: {body}")
        key, rest = body.split(":", 1)
        key = key.strip()
        rest = rest.strip()
        if not key:
            raise InvalidJob("yaml empty key")
        index += 1
        if rest:
            data[key] = _parse_scalar(rest)
            continue
        if index >= len(lines) or lines[index][0] <= indent:
            data[key] = {}
            continue
        nested, index = _parse_block(lines, index, indent + 2)
        data[key] = nested
    return data, index


def _parse_list(lines: list[tuple[int, str]], index: int, indent: int) -> tuple[list[object], int]:
    items: list[object] = []
    while index < len(lines):
        level, body = lines[index]
        if level < indent:
            break
        if level > indent:
            raise InvalidJob("yaml indent jumped")
        if not body.startswith("- "):
            raise InvalidJob("yaml expected list item")
        rest = body[2:].strip()
        index += 1
        if rest:
            if ":" in rest and not rest.startswith("{") and not _is_quoted(rest):
                key, value = rest.split(":", 1)
                nested = {key.strip(): _parse_scalar(value.strip()) if value.strip() else {}}
                if index < len(lines) and lines[index][0] > indent:
                    extra, index = _parse_map(lines, index, indent + 2)
                    if isinstance(nested.get(key.strip()), dict) and not nested[key.strip()]:
                        nested[key.strip()] = extra
                    else:
                        nested.update(extra)
                items.append(nested)
            else:
                items.append(_parse_scalar(rest))
            continue
        nested, index = _parse_block(lines, index, indent + 2)
        items.append(nested)
    return items, index


def _is_quoted(text: str) -> bool:
    return (text.startswith('"') and text.endswith('"')) or (
        text.startswith("'") and text.endswith("'")
    )


def _parse_scalar(text: str) -> object:
    if text in {"", "~", "null", "Null", "NULL"}:
        return None
    if text in {"true", "True", "TRUE"}:
        return True
    if text in {"false", "False", "FALSE"}:
        return False
    if _is_quoted(text):
        return text[1:-1]
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(part.strip()) for part in inner.split(",")]
    try:
        if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
            return int(text)
        return float(text)
    except ValueError:
        return text


def _dump(value: object, indent: int) -> list[str]:
    pad = " " * indent
    if isinstance(value, dict):
        if not value:
            return [f"{pad}" + "{}"]
        rows: list[str] = []
        for key, item in value.items():
            if isinstance(item, (dict, list)) and item:
                rows.append(f"{pad}{key}:")
                rows.extend(_dump(item, indent + 2))
            else:
                rows.append(f"{pad}{key}: {_scalar(item)}")
        return rows
    if isinstance(value, list):
        if not value:
            return [f"{pad}[]"]
        rows = []
        for item in value:
            if isinstance(item, dict) and item:
                first = True
                for key, nested in item.items():
                    prefix = "- " if first else "  "
                    first = False
                    if isinstance(nested, (dict, list)) and nested:
                        rows.append(f"{pad}{prefix}{key}:")
                        rows.extend(_dump(nested, indent + 4))
                    else:
                        rows.append(f"{pad}{prefix}{key}: {_scalar(nested)}")
            else:
                rows.append(f"{pad}- {_scalar(item)}")
        return rows
    return [f"{pad}{_scalar(value)}"]


def _scalar(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        if value == "" or any(ch in value for ch in ":#{}[]&*!|>'\"%@`"):
            return '"' + value.replace('"', '\\"') + '"'
        return value
    return str(value)
