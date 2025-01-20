"""Stdlib HTTP API for listing runs and kicking a job."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from riftlog.adapters.persistence.memory import MemoryStore
from riftlog.adapters.yaml.loader import parse_job
from riftlog.application.engine import Engine
from riftlog.domain.entities import JobSpec
from riftlog.security.auth import Gate, Token


class JobApi:
    def __init__(
        self,
        engine: Engine | None = None,
        store: MemoryStore | None = None,
        gate: Gate | None = None,
        jobs: dict[str, JobSpec] | None = None,
    ) -> None:
        self.engine = engine or Engine()
        self.store = store or MemoryStore()
        self.gate = gate or Gate()
        self.jobs = jobs or {}

    def handle(self, method: str, path: str, body: str, token: str = "") -> tuple[int, dict]:
        identity = self.gate.check(token) if self.gate.required else Token("anon", "admin")
        parsed = urlparse(path)
        route = parsed.path.rstrip("/") or "/"
        query = parse_qs(parsed.query)
        if method == "GET" and route == "/health":
            return 200, {"ok": True}
        if method == "GET" and route == "/runs":
            job = query.get("job", [None])[0]
            rows = self.store.list(job=job)
            return 200, {"runs": [_run_json(row) for row in rows]}
        if method == "GET" and route.startswith("/runs/"):
            run_id = route.split("/", 2)[-1]
            return 200, _run_json(self.store.get(run_id))
        if method == "POST" and route == "/runs":
            if not self.gate.can(identity, "run"):
                return 403, {"error": "forbidden"}
            payload = json.loads(body or "{}")
            spec_text = payload.get("yaml") or ""
            name = payload.get("job")
            if spec_text:
                job = parse_job(spec_text)
            elif name and name in self.jobs:
                job = self.jobs[name]
            else:
                return 400, {"error": "missing job"}
            run = self.engine.run(job, trigger="api")
            self.store.put(run)
            return 201, _run_json(run)
        return 404, {"error": "not found"}


def _run_json(run) -> dict:
    return {
        "run_id": run.run_id,
        "job": run.job,
        "state": run.state.value,
        "tenant_id": run.tenant_id,
        "steps": {name: result.state.value for name, result in run.results.items()},
    }


def make_server(api: JobApi, host: str = "127.0.0.1", port: int = 8080) -> ThreadingHTTPServer:
    outer = api

    class Handler(BaseHTTPRequestHandler):
        def _read(self) -> str:
            size = int(self.headers.get("Content-Length") or 0)
            if size <= 0:
                return ""
            return self.rfile.read(size).decode("utf-8")

        def _send(self, code: int, payload: dict) -> None:
            blob = json.dumps(payload).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(blob)))
            self.end_headers()
            self.wfile.write(blob)

        def do_GET(self) -> None:  # noqa: N802
            token = (self.headers.get("Authorization") or "").removeprefix("Bearer ").strip()
            code, payload = outer.handle("GET", self.path, "", token)
            self._send(code, payload)

        def do_POST(self) -> None:  # noqa: N802
            token = (self.headers.get("Authorization") or "").removeprefix("Bearer ").strip()
            code, payload = outer.handle("POST", self.path, self._read(), token)
            self._send(code, payload)

        def log_message(self, fmt: str, *args: object) -> None:
            return

    return ThreadingHTTPServer((host, port), Handler)
