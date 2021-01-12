"""
This module bonds the entry points (console scripts) to the argument parser
interface. By doing so, console scripts can either be bonded to:
    1. Raw python functions
    2. Different argument parsing solutions

New interfaces can be added by creating a submodule to this package and
exposing a "cli" function in that module. See the scenario examples below to
understand how to add the newly created interface to console scripts.

This module dynamically loads the submodules and exposes as its own attributes
the cli function of the submodules as the name of the submodule.
For example in the submodule "main.py" the "cli" function will be an attribute
of this module available for use/calling as "cli.main".

The following two scenarios are equivalent due to the dynamic sub module import
and attribute allocation.

Scenario 1:
  In Python modules/executables:
    from .cli import main
    main.cli()
  In setup.py or setup.cfg (recomended):
    console_scripts =
      my_script = {{ cookiecutter.project_slug }}.cli.main:cli

Scenario 2 (recomended):
  In Python modules/executables:
    from . import cli
    cli.main()
  In setup.py or setup.cfg (recomended):
    console_scripts =
      my_script = {{ cookiecutter.project_slug }}.cli:main

"""
import pkgutil
import importlib
import pathlib
import sys

for module in pkgutil.iter_modules(
        path=[pathlib.Path(__file__).parent.absolute()]):

    _cli = importlib.import_module(f".{module.name}", package=__name__)

    if hasattr(_cli, "cli"):
        setattr(sys.modules[__name__], module.name, _cli.cli)
    else:
        raise AttributeError(f'"{module.name}" module in cli does not have an'
                             ' cli attribute, required to interface with'
                             ' console scripts')

    del _cli
