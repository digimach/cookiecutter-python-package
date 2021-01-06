#!/usr/bin/env python
"""
{{ cookiecutter.project_title }}
=============
{{ cookiecutter.project_short_description }}

See README.md for more information.
"""
import os
import ast
import re
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

with open("src/{{ cookiecutter.project_slug | replace('-', '_') }}/__init__.py", encoding="utf8") as fp:
    version = re.search(r'__version__ = "(.*?)"', fp.read()).group(1)

setup(
    version=version,
    install_requires={{
        cookiecutter.install_requires.replace(" ", "").split(',')
    }},
    extras_require={
        "test": {{
            cookiecutter.project_extra_test_requires.replace(" ",
                                                             "").split(',')
        }},
        "dev": {{
            cookiecutter.project_extra_dev_requires.replace(" ", "").split(',')
        }}
    },
    zip_safe=False,
    platforms="any",
)