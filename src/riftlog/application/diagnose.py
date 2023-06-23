"""Heuristic diagnosis of a failed run. No network, no model calls."""

from __future__ import annotations

from riftlog.domain.entities import JobRun
from riftlog.domain.states import StepState


def diagnose(run: JobRun) -> list[str]:
    notes: list[str] = []
    failed = [row for row in run.results.values() if row.state == StepState.FAILED]
    skipped = [row for row in run.results.values() if row.state == StepState.SKIPPED]
    if not failed and run.state.value == "ok":
        notes.append("run finished clean")
        return notes
    if not failed:
        notes.append("run marked failed but no step result is failed")
        return notes
    for row in failed:
        err = row.error.lower()
        if "timeout" in err:
            notes.append(f"{row.name}: timeout, raise timeout_seconds or split the work")
        elif "connection" in err or "refused" in err:
            notes.append(f"{row.name}: downstream refused the socket")
        elif "retries exhausted" in err or row.attempts > 1:
            notes.append(f"{row.name}: died after {row.attempts} attempts: {row.error}")
        elif not row.error:
            notes.append(f"{row.name}: failed with an empty error string")
        else:
            notes.append(f"{row.name}: {row.error}")
    if skipped:
        names = ", ".join(row.name for row in skipped)
        notes.append(f"never started after the failure: {names}")
    return notes
