import click
from btc_stackexchange_markdown.parser import parse_data


@click.command()
@click.argument('id', type=int)
@click.argument('out', type=click.File('w'))
def cli(id, out):
    """Fetch the stackoverflow question and its answers
    export it as a markdown file.

    ID: the question ID

    OUT: the output file
    """
    click.echo(f'[-] Fetching data of question {id}')
    data = parse_data(id)
    click.echo(f'[*] Exporting to {out.name}')
    out.write(data)
    click.echo('[√] Done!')
