"""Filesystem helpers for CLI commands."""

from __future__ import annotations

from pathlib import Path


def ensure_dir(path: Path, dry_run: bool) -> str:
    """Ensure directory exists and return action name."""
    if path.exists():
        return "skipped"
    if not dry_run:
        path.mkdir(parents=True, exist_ok=True)
    return "created"


def ensure_file(path: Path, dry_run: bool, force: bool, content: str = "") -> str:
    """Create or overwrite a file and return action name."""
    if path.exists() and not force:
        return "skipped"

    if path.exists() and force:
        if not dry_run:
            path.write_text(content, encoding="utf-8")
        return "overwritten"

    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return "created"


def ensure_file_if_missing(path: Path, dry_run: bool, content: str = "") -> str:
    """Create file only when it does not exist."""
    if path.exists():
        return "skipped"
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return "created"
