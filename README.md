# riftlog

Local job runner. You write a YAML file with named steps, optional `needs`
edges, optional five-field cron, and optional retries. `riftlog run` (or
`Pipeline.run`) walks the DAG, calls Python functions from a catalog, and
stores the run. Stdlib only.

Python 3.10+. Package version `0.8.0`. CLI entry is `riftlog`.

## Install

```
pip install -e ".[dev]"
pytest -q
riftlog version
riftlog run examples/backup.yaml
riftlog run examples/backup.yaml --json --db runs.sqlite
riftlog new "preciso de um backup noturno"
```

`riftlog new` only picks among three local templates (`backup`, `etl`, `ping`).
It does not call a model.

## YAML spec

The parser lives under `riftlog.adapters.yaml`: maps, lists, scalars, `#`
comments, indent in multiples of 2. No tabs, tags, or anchors.

```yaml
name: nightly-backup
schedule: "30 2 * * *"
timezone: UTC
label: dumps then uploads
tenant: default          # also accepted as tenant_id; omit -> "default"
max_parallel: 0          # 0 means the whole ready batch
steps:
  dump:
    call: core.echo      # or `run:` — same field
    message: dump
    retries: 2
    retry_seconds: 1
    queue: default
    priority: 0
    cpu: 1
    memory_mb: 64
  upload:
    call: core.echo
    message: upload
    needs: [dump]        # or `requires:`; a single string is also a list of one
```

`steps` (alias `tasks`) may be a mapping (keys are names) or a list of
`{name, call, ...}` maps. Extra keys on a step go into the callable as kwargs,
merged under any nested `payload:` map.

## Layout

Packages follow ports-and-adapters:

- `domain` — JobSpec, graph, errors (no I/O)
- `ports` — Clock, RunStore, CatalogPort, Notifier
- `application` — Engine, Pipeline, catalog, retry, scheduler
- `adapters` — YAML, memory/sqlite stores, clocks, logs
- `cron` — five-field Agenda
- `security` — gate, rbac, vault, tenants, caps
- `workers` — dispatch queues and Worker
- `api` — stdlib HTTP
- `cli` — `riftlog` entry
- `tasks` — builtin callables registered on import

No third-party runtime dependencies.
