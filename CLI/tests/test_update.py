"""Tests for update command internals."""

from __future__ import annotations

from types import SimpleNamespace
from urllib.error import URLError

from nebu_cli.commands import update as update_cmd
from nebu_cli.commands.update import _compare_versions

def test_compare_versions_semver() -> None:
    assert _compare_versions("1.0.0", "1.1.0") == -1
    assert _compare_versions("1.2.0", "1.2.0") == 0
    assert _compare_versions("1.2.1", "1.2.0") == 1


def test_update_run_up_to_date(monkeypatch, capsys) -> None:
    monkeypatch.setattr(update_cmd, "get_local_version", lambda: "0.1.0")
    monkeypatch.setattr(update_cmd, "_fetch_latest_version", lambda: "0.1.0")

    exit_code = update_cmd.run(SimpleNamespace(apply=False, yes=False))
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "- status: atualizado" in output


def test_update_run_check_only_when_new_version_exists(monkeypatch, capsys) -> None:
    monkeypatch.setattr(update_cmd, "get_local_version", lambda: "0.1.0")
    monkeypatch.setattr(update_cmd, "_fetch_latest_version", lambda: "0.2.0")

    exit_code = update_cmd.run(SimpleNamespace(apply=False, yes=False))
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "- status: atualizacao disponivel" in output
    assert "apply_command" in output


def test_update_run_apply_yes_executes_apply(monkeypatch) -> None:
    monkeypatch.setattr(update_cmd, "get_local_version", lambda: "0.1.0")
    monkeypatch.setattr(update_cmd, "_fetch_latest_version", lambda: "0.2.0")
    monkeypatch.setattr(update_cmd, "_apply_update", lambda: 7)

    exit_code = update_cmd.run(SimpleNamespace(apply=True, yes=True))
    assert exit_code == 7


def test_update_run_apply_cancelled_by_confirmation(monkeypatch, capsys) -> None:
    monkeypatch.setattr(update_cmd, "get_local_version", lambda: "0.1.0")
    monkeypatch.setattr(update_cmd, "_fetch_latest_version", lambda: "0.2.0")
    monkeypatch.setattr(update_cmd, "_confirm_apply", lambda: False)

    called = {"value": False}

    def fake_apply_update() -> int:
        called["value"] = True
        return 0

    monkeypatch.setattr(update_cmd, "_apply_update", fake_apply_update)

    exit_code = update_cmd.run(SimpleNamespace(apply=True, yes=False))
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "- apply: cancelado" in output
    assert called["value"] is False


def test_update_run_returns_error_when_pypi_lookup_fails(monkeypatch, capsys) -> None:
    monkeypatch.setattr(update_cmd, "get_local_version", lambda: "0.1.0")

    def fake_fetch_latest_version() -> str:
        raise URLError("offline")

    monkeypatch.setattr(update_cmd, "_fetch_latest_version", fake_fetch_latest_version)

    exit_code = update_cmd.run(SimpleNamespace(apply=False, yes=False))
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "falha ao consultar PyPI" in output
