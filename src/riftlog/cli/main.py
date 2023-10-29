"""CLI: riftlog run <file.yaml>."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from riftlog.adapters.persistence.sqlite import SqliteStore
from riftlog.adapters.yaml.loader import load_job
from riftlog.application.diagnose import diagnose
from riftlog.application.engine import Engine
from riftlog.application.generate import generate
from riftlog import tasks as _tasks  # noqa: F401


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="riftlog")
    sub = parser.add_subparsers(dest="cmd", required=True)
    run_p = sub.add_parser("run")
    run_p.add_argument("spec")
    run_p.add_argument("--db", default="")
    run_p.add_argument("--json", action="store_true")
    gen_p = sub.add_parser("new")
    gen_p.add_argument("wish")
    sub.add_parser("version")
    args = parser.parse_args(argv)
    if args.cmd == "version":
        from riftlog import __version__

        print(__version__)
        return 0
    if args.cmd == "new":
        sys.stdout.write(generate(args.wish))
        return 0
    job = load_job(args.spec)
    run = Engine().run(job)
    if args.db:
        SqliteStore(args.db).put(run)
    if args.json:
        sys.stdout.write(
            json.dumps(
                {
                    "run_id": run.run_id,
                    "state": run.state.value,
                    "diagnose": diagnose(run),
                }
            )
            + "\n"
        )
    else:
        print(run.run_id, run.state.value)
        for line in diagnose(run):
            print(line)
    return 0 if run.state.value == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
