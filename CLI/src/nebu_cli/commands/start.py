"""Implementation of `nebu start`."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from nebu_cli import __version__
from nebu_cli.core.fs import ensure_dir, ensure_file, ensure_file_if_missing
from nebu_cli.core.manifest import MANIFEST_FILE, build_manifest, load_manifest
from nebu_cli.core.manifest import save_manifest
from nebu_cli.specs.structure import DOC_FILES, REQUIRED_DIRS, resolve_path


@dataclass
class StartResult:
    """Track filesystem actions from start command."""

    created: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    overwritten: list[str] = field(default_factory=list)

    def add(self, action: str, path: Path) -> None:
        rel = str(path)
        if action == "created":
            self.created.append(rel)
        elif action == "overwritten":
            self.overwritten.append(rel)
        else:
            self.skipped.append(rel)


def _target_root(root_arg: str) -> Path:
    return Path(root_arg).expanduser().resolve()


def _track(action: str, path: Path, result: StartResult) -> None:
    result.add(action, path)


def _create_dirs(root: Path, dry_run: bool, result: StartResult) -> None:
    for rel in REQUIRED_DIRS:
        path = resolve_path(root, rel)
        action = ensure_dir(path, dry_run=dry_run)
        _track(action, path, result)


def _create_files(
    root: Path,
    dry_run: bool,
    force: bool,
    result: StartResult,
) -> None:
    guide_path = resolve_path(root, "GUIDE.md")
    action = ensure_file_if_missing(guide_path, dry_run=dry_run, content="")
    _track(action, guide_path, result)

    for rel in DOC_FILES:
        file_path = resolve_path(root, rel)
        action = ensure_file(file_path, dry_run=dry_run, force=force, content="")
        _track(action, file_path, result)


def _write_manifest(
    root: Path,
    profile: str,
    dry_run: bool,
    result: StartResult,
) -> None:
    manifest_path = resolve_path(root, MANIFEST_FILE)
    existing = load_manifest(manifest_path)
    payload = build_manifest(
        existing=existing,
        profile=profile,
        root=root,
        nebula_version=__version__,
    )
    action = save_manifest(manifest_path, payload=payload, dry_run=dry_run)
    _track(action, manifest_path, result)


def _print_section(name: str, items: list[str]) -> None:
    print(f"{name}: {len(items)}")
    for item in items:
        print(f"- {item}")


def run(args) -> int:
    """Execute bootstrap structure creation."""
    root = _target_root(args.root)
    result = StartResult()

    _create_dirs(root=root, dry_run=args.dry_run, result=result)
    _create_files(
        root=root,
        dry_run=args.dry_run,
        force=args.force,
        result=result,
    )
    _write_manifest(
        root=root,
        profile=args.profile,
        dry_run=args.dry_run,
        result=result,
    )

    print("summary:")
    print(f"- root: {root}")
    print(f"- profile: {args.profile}")
    print(f"- dry_run: {args.dry_run}")
    print(f"- force: {args.force}")
    _print_section("created", result.created)
    _print_section("skipped", result.skipped)
    _print_section("overwritten", result.overwritten)
    return 0
