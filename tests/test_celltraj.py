"""Basic package and CLI tests for celltraj."""

from click.testing import CliRunner

import celltraj
from celltraj import cli


def test_package_exposes_version():
    assert celltraj.__version__


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "celltraj" in result.output

    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help" in help_result.output
