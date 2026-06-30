"""Console script for celltraj."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for celltraj."""
    click.echo("celltraj: single-cell trajectory modeling utilities")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
