"""Manifest read/write helpers."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MANIFEST_FILE = ".nebula/manifest.json"


def utc_now_iso() -> str:
    """Return current UTC timestamp in ISO-8601 format."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_manifest(path: Path) -> dict[str, Any] | None:
    """Load manifest if present and valid."""
    if not path.exists():
        return None
    try:
        content = path.read_text(encoding="utf-8")
        data = json.loads(content)
    except (json.JSONDecodeError, OSError):
        return None
    return data if isinstance(data, dict) else None


def build_manifest(
    existing: dict[str, Any] | None,
    profile: str,
    root: Path,
    nebula_version: str,
) -> dict[str, Any]:
    """Build manifest payload preserving created_at when possible."""
    now = utc_now_iso()
    created_at = existing.get("created_at") if existing else now
    return {
        "nebula_version": nebula_version,
        "profile": profile,
        "created_at": created_at,
        "last_run_at": now,
        "root": str(root),
    }


def save_manifest(path: Path, payload: dict[str, Any], dry_run: bool) -> str:
    """Persist manifest and return action name."""
    action = "overwritten" if path.exists() else "created"
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        path.write_text(text, encoding="utf-8")
    return action
