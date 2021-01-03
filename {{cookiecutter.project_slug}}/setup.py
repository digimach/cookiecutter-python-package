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

setup(
    name="{{ cookiecutter.project_slug | replace('_', '-') }}",
    version="",
    url="{{ cookiecutter.project_source_url }}",
    project_urls={
        "Code": "{{ cookiecutter.project_source_url }}",
        "Documentation": "{{ cookiecutter.project_doc_url }}"
    },
    license="{{ cookiecutter.project_license }}",
    author="{{ cookiecutter.project_author_name }}",
    author_email="{{ cookiecutter.project_author_email }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=__doc__,
    classifiers=[
        "License :: {{ cookiecutter.project_license }}",
        "Programming Language :: Python",
        "Programming Language :: Python :: {{ cookiecutter.project_python_version }}",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(exclude=("tests", )),
    include_package_data=True,
    python_requires=">={{ cookiecutter.project_python_version }}",
    install_requires={{
        cookiecutter.install_requires.replace(" ", "").split(',')
    }},
    extras_require={
        "test": {{
            cookiecutter.project_extra_test_requires.replace(" ",
                                                             "").split(',')
        }},
        "dev":
        {{cookiecutter.project_extra_dev_requires.replace(" ", "").split(',')}}
    },
    zip_safe=False,
    platforms="any",
)
