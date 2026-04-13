"""Implementation of `nebu update`."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from urllib.error import URLError
from urllib.request import urlopen

from nebu_cli.commands.version import get_local_version


PACKAGE_NAME = "nebula-spec-kit-cli"
PYPI_ENDPOINT = f"https://pypi.org/pypi/{PACKAGE_NAME}/json"


def _parse_version(value: str) -> tuple[int, int, int, str] | None:
    cleaned = value.strip().removeprefix("v")
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)(.*)$", cleaned)
    if not match:
        return None
    major, minor, patch, suffix = match.groups()
    return int(major), int(minor), int(patch), suffix


def _compare_versions(local: str, latest: str) -> int:
    local_parts = _parse_version(local)
    latest_parts = _parse_version(latest)

    if local_parts is None or latest_parts is None:
        if local == latest:
            return 0
        return -1 if local < latest else 1

    local_semver = local_parts[:3]
    latest_semver = latest_parts[:3]
    if local_semver < latest_semver:
        return -1
    if local_semver > latest_semver:
        return 1

    local_suffix = local_parts[3]
    latest_suffix = latest_parts[3]
    if local_suffix == latest_suffix:
        return 0
    if local_suffix and not latest_suffix:
        return -1
    if latest_suffix and not local_suffix:
        return 1
    return -1 if local_suffix < latest_suffix else 1


def _fetch_latest_version() -> str:
    with urlopen(PYPI_ENDPOINT, timeout=6) as response:
        payload = json.loads(response.read().decode("utf-8"))
    info = payload.get("info", {})
    latest = info.get("version")
    if not isinstance(latest, str) or not latest.strip():
        raise ValueError("resposta do PyPI sem versao")
    return latest.strip()


def _confirm_apply() -> bool:
    answer = input("Aplicar atualizacao agora? [y/N]: ").strip().lower()
    return answer in {"y", "yes", "s", "sim"}


def _apply_update() -> int:
    command = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        PACKAGE_NAME,
    ]
    print("update:")
    print(f"- command: {' '.join(command)}")
    completed = subprocess.run(command, check=False)
    return completed.returncode


def run(args) -> int:
    """Check latest package on PyPI and optionally update."""
    local = get_local_version()
    try:
        latest = _fetch_latest_version()
    except (URLError, ValueError, TimeoutError) as exc:
        print("update:")
        print(f"- error: falha ao consultar PyPI ({exc})")
        return 1

    print("update:")
    print(f"- local: {local}")
    print(f"- latest: {latest}")

    relation = _compare_versions(local=local, latest=latest)
    if relation >= 0:
        if relation == 0:
            print("- status: atualizado")
        else:
            print("- status: versao local acima do PyPI")
        return 0

    print("- status: atualizacao disponivel")
    print(f"- apply_command: python -m pip install --upgrade {PACKAGE_NAME}")

    if not args.apply:
        return 0

    if not args.yes and not _confirm_apply():
        print("- apply: cancelado")
        return 0

    return _apply_update()
