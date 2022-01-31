import click
from click.testing import CliRunner

import cli

def test_sync():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['--option', 'function'], input='test')
    assert result.exit_code == 0
