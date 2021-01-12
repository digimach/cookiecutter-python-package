"""
This module holds the console script argument schema for the main script of
{{ cookiecutter.project_slug }} which can be invoked by {{ cookiecutter.project_slug.replace('_', '-') }}
"""
import platform
import sys
import click

from .. import __version__


def cli():
    """
    Main CLI interface exposed to the cli module and exposed to the console
    script.
    """
    click.echo(f"Calling {sys.argv[0]}")


@click.command()
def run():
    """
    The function that gets invoked by the subcommand "run"
    """
    click.echo('Running the script')


@click.command()
def version():
    """
    The function that gets invoked by the subcommand "version"
    """
    click.echo(f"Python {platform.python_version()}\n"
               f"{{ cookiecutter.project_slug }} {__version__}")


cli.add_command(run)  # pylint: disable=no-member
cli.add_command(version)  # pylint: disable=no-member
