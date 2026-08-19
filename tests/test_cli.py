from riftlog.cli import main
from riftlog.domain.states import RunState
from riftlog.adapters.persistence import SqliteStore
from riftlog import __version__


def test_cli_run_text(tmp_path, capsys):
    path = tmp_path / "ping.yaml"
    path.write_text(
        "name: ping\nsteps:\n  ping:\n    call: core.echo\n    message: hi\n",
        encoding="utf-8",
    )
    assert main(["run", str(path)]) == 0
    out = capsys.readouterr().out
    assert "ok" in out
    assert "run finished clean" in out


def test_cli_run_json_and_db(tmp_path, capsys):
    path = tmp_path / "ping.yaml"
    path.write_text(
        "name: ping\nsteps:\n  ping:\n    call: core.echo\n    message: hi\n",
        encoding="utf-8",
    )
    db = tmp_path / "runs.sqlite"
    assert main(["run", str(path), "--json", "--db", str(db)]) == 0
    out = capsys.readouterr().out
    assert '"state": "ok"' in out
    store = SqliteStore(db)
    assert store.list("ping")[0].state == RunState.OK


def test_cli_failed_job_exits_one(tmp_path, capsys):
    path = tmp_path / "boom.yaml"
    path.write_text(
        "name: boom\nsteps:\n  bad:\n    call: core.fail\n    reason: nope\n",
        encoding="utf-8",
    )
    assert main(["run", str(path)]) == 1
    out = capsys.readouterr().out
    assert "failed" in out
    assert "nope" in out


def test_cli_new_backup(capsys):
    assert main(["new", "preciso de um backup noturno"]) == 0
    out = capsys.readouterr().out
    assert "dump" in out
    assert "upload" in out


def test_cli_new_etl(capsys):
    assert main(["new", "etl extract"]) == 0
    assert "extract" in capsys.readouterr().out


def test_cli_version(capsys):
    assert main(["version"]) == 0
    assert capsys.readouterr().out.strip() == __version__
