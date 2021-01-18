#!/usr/bin/env python
"""
{{ cookiecutter.project_title }}
=============
{{ cookiecutter.project_short_description }}

See README.md for more information.
"""
import re

from setuptools import setup

with open("src/{{ cookiecutter.project_slug }}/__init__.py", encoding="utf8") as fp:
    version = re.search(r'__version__ = "(.*?)"', fp.read()).group(1)

extra_requires = {
    "dev": {{cookiecutter.project_extra_dev_requires.replace(" ", "").split(",")}},
    "lint": {{cookiecutter.project_extra_lint_requires.replace(" ", "").split(",")}},
    "test": {{cookiecutter.project_extra_test_requires.replace(" ", "").split(",")}},
}

setup(
    version=version,
    install_requires={{cookiecutter.install_requires.replace(" ", "").split(",")}},
    extras_require=extra_requires,
    zip_safe=False,
    platforms="any",
)
