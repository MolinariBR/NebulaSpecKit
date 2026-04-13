"""Tests for start command behavior."""

from __future__ import annotations

import tempfile
from pathlib import Path

from nebu_cli.__main__ import main


def test_start_dry_run_does_not_create_files() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        exit_code = main(["start", "--root", str(root), "--dry-run"])

        assert exit_code == 0
        assert not (root / "Docs").exists()
        assert not (root / ".nebula").exists()
