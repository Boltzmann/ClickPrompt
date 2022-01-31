import click
from click.testing import CliRunner

import cli

def test_sync():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['--debug', 'sync', input='test'])
    assert result.exit_code == 0
    assert 'Debug mode is on' in result.output
    assert 'Syncing' in result.output
