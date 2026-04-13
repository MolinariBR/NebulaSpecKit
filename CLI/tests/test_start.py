"""Tests for start command behavior."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from nebu_cli.__main__ import main
from nebu_cli.specs.structure import DOC_FILES, REQUIRED_DIRS


def test_start_dry_run_does_not_create_files() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        exit_code = main(["start", "--root", str(root), "--dry-run"])

        assert exit_code == 0
        assert not (root / "Docs").exists()
        assert not (root / ".nebula").exists()


def test_start_creates_expected_structure_and_manifest() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        exit_code = main(["start", "--root", str(root)])

        assert exit_code == 0

        for rel in REQUIRED_DIRS:
            assert (root / rel).is_dir()

        guide = root / "Guide-Started.md"
        assert guide.is_file()
        assert guide.read_text(encoding="utf-8") == ""

        for rel in DOC_FILES:
            path = root / rel
            assert path.is_file()
            assert path.read_text(encoding="utf-8") == ""

        manifest_path = root / ".nebula" / "manifest.json"
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert payload["profile"] == "full"
        assert payload["root"] == str(root)
        assert payload["created_at"]
        assert payload["last_run_at"]


def test_start_idempotent_without_force_preserves_existing_docs() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        assert main(["start", "--root", str(root)]) == 0

        brief = root / "Docs" / "brief.md"
        brief.write_text("conteudo customizado", encoding="utf-8")

        assert main(["start", "--root", str(root)]) == 0
        assert brief.read_text(encoding="utf-8") == "conteudo customizado"


def test_start_force_overwrites_existing_docs() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        assert main(["start", "--root", str(root)]) == 0

        brief = root / "Docs" / "brief.md"
        brief.write_text("conteudo customizado", encoding="utf-8")

        assert main(["start", "--root", str(root), "--force"]) == 0
        assert brief.read_text(encoding="utf-8") == ""
