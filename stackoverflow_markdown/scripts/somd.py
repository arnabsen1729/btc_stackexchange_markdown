import click


@click.command()
@click.argument('id')
@click.argument('out', type=click.File('w'))
def cli(id, out):
    """Fetch the stackoverflow question and its answers
    export it as a markdown file.

    ID: the question ID

    OUT: the output file
    """
    click.echo(f'Args passed {id} {out}')
