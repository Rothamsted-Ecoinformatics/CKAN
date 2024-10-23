import click


@click.group(short_help="customapi CLI.")
def customapi():
    """customapi CLI.
    """
    pass


@customapi.command()
@click.argument("name", default="customapi")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [customapi]
