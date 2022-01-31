import click

@click.group()
@click.option('--option/--no-option', default=False)
def cli(option):
    click.echo(click.prompt('Type something'))
    click.echo(click.prompt('Type something else'))
    click.echo('Option is %s' % ('on' if option else 'off'))

@cli.command()
def function():
    click.echo('Functioning')
