from riftlog.domain.errors import CycleInGraph, UnknownStep
from riftlog.domain.graph import layers, ready_names, topo_order
from riftlog.domain.entities import JobSpec, StepSpec
import pytest


def job(*pairs: tuple[str, list[str]]) -> JobSpec:
    steps = [StepSpec(name=name, call="core.echo", needs=needs) for name, needs in pairs]
    return JobSpec(name="g", steps=steps)


def test_topo_linear():
    spec = job(("a", []), ("b", ["a"]), ("c", ["b"]))
    assert topo_order(spec) == ["a", "b", "c"]


def test_ready_after_first():
    spec = job(("a", []), ("b", ["a"]), ("c", ["a"]))
    assert ready_names(spec, set()) == ["a"]
    assert ready_names(spec, {"a"}) == ["b", "c"]


def test_unknown_need():
    spec = job(("a", ["ghost"]))
    with pytest.raises(UnknownStep):
        topo_order(spec)


def test_cycle():
    spec = job(("a", ["b"]), ("b", ["a"]))
    with pytest.raises(CycleInGraph):
        topo_order(spec)


def test_layers_diamond():
    spec = job(("a", []), ("b", ["a"]), ("c", ["a"]), ("d", ["b", "c"]))
    assert layers(spec) == [["a"], ["b", "c"], ["d"]]


def test_self_need():
    spec = job(("a", ["a"]))
    with pytest.raises(Exception):
        topo_order(spec)
