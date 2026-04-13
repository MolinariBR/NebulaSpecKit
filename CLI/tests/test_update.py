"""Tests for update command internals."""

from __future__ import annotations

from nebu_cli.commands.update import _compare_versions


def test_compare_versions_semver() -> None:
    assert _compare_versions("1.0.0", "1.1.0") == -1
    assert _compare_versions("1.2.0", "1.2.0") == 0
    assert _compare_versions("1.2.1", "1.2.0") == 1
