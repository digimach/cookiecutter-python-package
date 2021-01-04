#!/bin/env python3
"""
Cookiecutter pre generation hook script that handles operations before the
template project is used to generate a target project.
"""
import re
import sys


def check_python_min_max_versions():
    """
    Check to make sure project_python_min_version and
    project_python_max_version are valid.
    """

    project_python_min_version = {{cookiecutter.project_python_min_version}}  # noqa pylint: disable=undefined-variable
    project_python_max_version = {{cookiecutter.project_python_max_version}}  # noqa pylint: disable=undefined-variable
    project_valid_python_versions = "{{cookiecutter.project_valid_python_versions}}".replace(" ", "").split(",")  # noqa pylint: disable=line-too-long

    if not re.search(r'\d+.\d+', str(project_python_min_version)):
        print(('** ERROR: Invalid value provided for'
               ' "project_python_min_version".'))
        sys.exit(1)
    elif not re.search(r'\d+.\d+', str(project_python_max_version)):
        print(('** ERROR: Invalid value provided for'
               ' "project_python_max_version".'))
        sys.exit(1)
    elif str(project_python_min_version) not in project_valid_python_versions:
        print(('** ERROR: Invalid value provided for'
               f' "project_python_min_version" {project_python_min_version}.'
               f' Expecting on of: {project_valid_python_versions}'))
        sys.exit(1)
    elif str(project_python_max_version) not in project_valid_python_versions:
        print(('** ERROR: Invalid value provided for'
               ' "project_python_max_version"'
               f' {project_python_max_version}.'
               f' Expecting on of: {project_valid_python_versions}'))
        sys.exit(1)

    if project_python_min_version > project_python_max_version:
        print(('** ERROR: "project_python_min_version" (%s) has to be greater'
               ' than or equal to "project_python_max_version" (%s)') %
              project_python_min_version, project_python_max_version)
        sys.exit(1)


if __name__ == '__main__':
    check_python_min_max_versions()
