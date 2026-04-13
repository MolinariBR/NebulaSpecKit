"""Tests for version command."""

from __future__ import annotations

from nebu_cli.__main__ import main
from nebu_cli import __version__
from nebu_cli.commands import version as version_cmd


def test_version_command_returns_zero() -> None:
    exit_code = main(["version"])
    assert exit_code == 0


def test_get_local_version_falls_back_to_package_version(monkeypatch) -> None:
    def fake_version(_package_name: str) -> str:
        raise version_cmd.PackageNotFoundError

    monkeypatch.setattr(version_cmd, "version", fake_version)
    assert version_cmd.get_local_version() == __version__


def test_get_local_version_uses_first_available_package(monkeypatch) -> None:
    calls: list[str] = []

    def fake_version(package_name: str) -> str:
        calls.append(package_name)
        if package_name == "nebula-spec-kit-cli":
            return "9.9.9"
        raise version_cmd.PackageNotFoundError

    monkeypatch.setattr(version_cmd, "version", fake_version)

    assert version_cmd.get_local_version() == "9.9.9"
    assert calls == ["nebula-spec-kit-cli"]
