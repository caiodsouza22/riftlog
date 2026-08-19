from riftlog.adapters.yaml import parse_job
from riftlog.application.engine import Engine


def main() -> None:
    job = parse_job(
        """
name: ping
steps:
  ping:
    call: core.echo
    message: pong
"""
    )
    run = Engine().run(job)
    print(run.run_id, run.state.value, run.results["ping"].output)


if __name__ == "__main__":
    main()
