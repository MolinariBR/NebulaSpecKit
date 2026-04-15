"""Entrypoint for Nebula CLI."""

from __future__ import annotations

import argparse

from nebu_cli.commands import start, submit, update, version

def build_parser() -> argparse.ArgumentParser:
    """Build root parser and subcommands."""
    parser = argparse.ArgumentParser(prog="nebu")
    subparsers = parser.add_subparsers(dest="command")

    submit_parser = subparsers.add_parser(
        "submit",
        help="Automatiza qualidade, commit e tracking no Docs/tasks.md",
    )
    submit_parser.add_argument(
        "message",
        help="Mensagem do commit da task",
    )
    submit_parser.add_argument(
        "--task-id",
        required=False,
        help="ID opcional da task no formato (Ex: TASK-001)",
    )
    submit_parser.set_defaults(handler=submit.run)

    start_parser = subparsers.add_parser(
        "start",
        help="Inicializa estrutura Nebula no projeto alvo",
    )
    start_parser.add_argument(
        "--profile",
        default="full",
        choices=["full", "quick"],
        help="Perfil de bootstrap (default: full)",
    )
    start_parser.add_argument(
        "--root",
        default=".",
        help="Diretorio alvo (default: diretorio atual)",
    )
    start_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula sem escrever no disco",
    )
    start_parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescreve arquivos Docs existentes",
    )
    start_parser.set_defaults(handler=start.run)

    version_parser = subparsers.add_parser(
        "version",
        help="Exibe versao instalada",
    )
    version_parser.set_defaults(handler=version.run)

    update_parser = subparsers.add_parser(
        "update",
        help="Verifica versao mais recente no PyPI",
    )
    update_parser.add_argument(
        "--apply",
        action="store_true",
        help="Aplica atualizacao do pacote",
    )
    update_parser.add_argument(
        "--yes",
        action="store_true",
        help="Nao pedir confirmacao ao aplicar update",
    )
    update_parser.set_defaults(handler=update.run)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run CLI command and return exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "command", None):
        parser.print_help()
        return 0

    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
