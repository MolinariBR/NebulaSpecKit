"""Tests for version command."""

from __future__ import annotations

from nebu_cli.__main__ import main


def test_version_command_returns_zero() -> None:
    exit_code = main(["version"])
    assert exit_code == 0
