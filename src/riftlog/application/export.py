"""Export a run as JSON or as a tiny YAML report."""

from __future__ import annotations

import json

from riftlog.adapters.yaml.parser import dump_yaml
from riftlog.domain.entities import JobRun


def run_to_dict(run: JobRun) -> dict[str, object]:
    return {
        "run_id": run.run_id,
        "job": run.job,
        "state": run.state.value,
        "tenant_id": run.tenant_id,
        "trigger": run.trigger,
        "results": {
            name: {
                "state": result.state.value,
                "attempts": result.attempts,
                "error": result.error,
                "output": result.output,
            }
            for name, result in run.results.items()
        },
    }


def run_to_json(run: JobRun) -> str:
    return json.dumps(run_to_dict(run), indent=2) + "\n"


def run_to_yaml(run: JobRun) -> str:
    return dump_yaml(run_to_dict(run))
