Adding console scripts
#######################

Before adding a console script
******************************

1. Make sure the name of the script is not going to conflict with any
   application including ``{{ cookiecutter.project_slug }}``.

2. Pick a reasonable name for the console script.

3. Try grouping multiple commands either into existing console scripts or the
   new one you create. For example::

    my_script run
    my_script check
    my_script log

   This creates one console script and multiple groups/sub-commands, limiting
   the number of console scripts exposed.

Adding a console script
***********************

Adding a new executable script that users can invoke from command line after
installing can be done by adding an entry in ``setup.cfg``::

    console_scripts =
        ..
        <executable_name> = {{ cookiecutter.project_slug }}.cli:<sub_module>

You then need to write the function in
``/src/{{ cookiecutter.project_slug }}cli/<sub_module>.py`` called ``cli``.

The ``cli`` function in should be able to handle the call made by the console
script and can use any argument parser.

Here is an example of the ``cli`` function which uses `click`_::

    """
    This module holds the console script argument schema for the
    <executable_name> script of {{ cookiecutter.project_slug }}.
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
