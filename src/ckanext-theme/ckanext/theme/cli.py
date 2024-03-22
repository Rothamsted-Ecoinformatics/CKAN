import click


@click.group(short_help="theme CLI.")
def theme():
    """theme CLI.
    """
    pass


@theme.command()
@click.argument("name", default="theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [theme]
