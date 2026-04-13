"""Canonical filesystem structure for Nebula bootstrap."""

from __future__ import annotations

from pathlib import Path

REQUIRED_DIRS = (
    ".nebula",
    "Docs",
    "Docs/Prototype",
)

DOC_FILES = (
    "Docs/brief.md",
    "Docs/project.md",
    "Docs/stack.md",
    "Docs/user-stories.md",
    "Docs/pages.md",
    "Docs/flow.md",
    "Docs/design-system.md",
    "Docs/tokens.json",
    "Docs/entities.md",
    "Docs/architecture.md",
    "Docs/contract.yaml",
    "Docs/structure.md",
    "Docs/deploy.md",
    "Docs/plan.md",
    "Docs/tasks.md",
    "Docs/control.md",
)

REQUIRED_FILES = ("GUIDE.md", *DOC_FILES)


def resolve_path(root: Path, rel_path: str) -> Path:
    """Resolve a repository-relative path from root."""
    return root / rel_path
