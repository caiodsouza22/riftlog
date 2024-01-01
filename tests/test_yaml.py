from riftlog.domain.errors import InvalidJob
from riftlog.adapters.yaml import dump_yaml, parse_yaml
import pytest


def test_map_and_list():
    data = parse_yaml(
        """
name: demo
steps:
  - name: a
    call: core.echo
  - name: b
    call: core.add
items:
  - one
  - two
flag: true
count: 3
empty:
"""
    )
    assert data["name"] == "demo"
    assert data["flag"] is True
    assert data["count"] == 3
    assert data["items"] == ["one", "two"]
    assert data["steps"][0]["name"] == "a"


def test_nested_map():
    data = parse_yaml(
        """
outer:
  inner:
    value: 9
"""
    )
    assert data["outer"]["inner"]["value"] == 9


def test_dump_roundtrip_scalars():
    text = dump_yaml({"name": "x", "ok": True, "n": 2, "missing": None})
    data = parse_yaml(text)
    assert data["name"] == "x"
    assert data["ok"] is True
    assert data["n"] == 2
    assert data["missing"] is None


def test_tabs_rejected():
    with pytest.raises(InvalidJob):
        parse_yaml("name:\thello")


def test_odd_indent_rejected():
    with pytest.raises(InvalidJob):
        parse_yaml("a:\n b: 1\n")


def test_quoted_string():
    data = parse_yaml('title: "hello: world"\n')
    assert data["title"] == "hello: world"


def test_null_and_bool_forms():
    data = parse_yaml("a: null\nb: FALSE\nc: True\n")
    assert data["a"] is None
    assert data["b"] is False
    assert data["c"] is True
