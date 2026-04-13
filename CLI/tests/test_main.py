"""Tests for parser and main routing."""

from __future__ import annotations

from nebu_cli.__main__ import build_parser, main


def test_main_without_command_prints_help(capsys) -> None:
    exit_code = main([])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "usage: nebu" in output


def test_parser_registers_expected_subcommands() -> None:
    parser = build_parser()
    args = parser.parse_args(["start"])
    assert args.command == "start"

    args = parser.parse_args(["version"])
    assert args.command == "version"

    args = parser.parse_args(["update"])
    assert args.command == "update"
