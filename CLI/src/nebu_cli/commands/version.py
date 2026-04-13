"""Implementation of `nebu version`."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from nebu_cli import __version__


PACKAGE_NAMES = (
    "nebula-spec-kit-cli",
    "nebu",
    "nebu-cli",
)


def get_local_version() -> str:
    """Read installed package version with fallback."""
    for package_name in PACKAGE_NAMES:
        try:
            return version(package_name)
        except PackageNotFoundError:
            continue
    return __version__


def run(_args) -> int:
    """Print CLI version."""
    local_version = get_local_version()
    print("version:")
    print(f"- local: {local_version}")
    return 0
