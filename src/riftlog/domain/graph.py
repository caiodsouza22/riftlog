"""Step graph: needs[], ready set, cycle detection. Pure functions."""

from __future__ import annotations

from riftlog.domain.entities import JobSpec, StepSpec
from riftlog.domain.errors import CycleInGraph, InvalidJob, UnknownStep


def step_map(job: JobSpec) -> dict[str, StepSpec]:
    return job.by_name()


def validate_needs(job: JobSpec) -> None:
    names = set(step_map(job))
    for step in job.steps:
        for dep in step.needs:
            if dep not in names:
                raise UnknownStep(dep)
            if dep == step.name:
                raise InvalidJob(f"{step.name} depends on itself")
    _assert_acyclic(job)


def predecessors(job: JobSpec) -> dict[str, set[str]]:
    return {step.name: set(step.needs) for step in job.steps}


def successors(job: JobSpec) -> dict[str, set[str]]:
    pred = predecessors(job)
    succ: dict[str, set[str]] = {name: set() for name in pred}
    for name, deps in pred.items():
        for dep in deps:
            if dep in succ:
                succ[dep].add(name)
    return succ


def ready_names(job: JobSpec, done: set[str]) -> list[str]:
    pred = predecessors(job)
    ready = [name for name, deps in pred.items() if name not in done and deps <= done]
    order = {step.name: index for index, step in enumerate(job.steps)}
    ready.sort(key=lambda name: (order[name], name))
    return ready


def topo_order(job: JobSpec) -> list[str]:
    validate_needs(job)
    pred = {name: set(deps) for name, deps in predecessors(job).items()}
    order_index = {step.name: index for index, step in enumerate(job.steps)}
    ready = [name for name, deps in pred.items() if not deps]
    ready.sort(key=lambda name: (order_index[name], name))
    seen: list[str] = []
    while ready:
        name = ready.pop(0)
        seen.append(name)
        for other, deps in pred.items():
            if name in deps:
                deps.remove(name)
                if not deps and other not in seen and other not in ready:
                    ready.append(other)
                    ready.sort(key=lambda item: (order_index[item], item))
    if len(seen) != len(pred):
        leftover = [name for name in pred if name not in seen]
        raise CycleInGraph(leftover)
    return seen


def layers(job: JobSpec) -> list[list[str]]:
    """Group steps into parallel waves by remaining predecessors."""
    validate_needs(job)
    pred = {name: set(deps) for name, deps in predecessors(job).items()}
    order_index = {step.name: index for index, step in enumerate(job.steps)}
    remaining = set(pred)
    waves: list[list[str]] = []
    while remaining:
        wave = [name for name in remaining if not pred[name]]
        if not wave:
            raise CycleInGraph(sorted(remaining))
        wave.sort(key=lambda name: (order_index[name], name))
        waves.append(wave)
        for name in wave:
            remaining.remove(name)
            for other in remaining:
                pred[other].discard(name)
    return waves


def _assert_acyclic(job: JobSpec) -> None:
    pred = {name: set(deps) for name, deps in predecessors(job).items()}
    ready = [name for name, deps in pred.items() if not deps]
    seen: set[str] = set()
    while ready:
        name = ready.pop()
        seen.add(name)
        for other, deps in pred.items():
            if name in deps:
                deps.remove(name)
                if not deps and other not in seen and other not in ready:
                    ready.append(other)
    if len(seen) != len(pred):
        leftover = [name for name in pred if name not in seen]
        raise CycleInGraph(leftover)
