#!/bin/env python3
"""
Cookiecutter post generation hook script that handles operations after the
template project is used to generate a target project.
"""

import shutil
import os


def set_license():
    """
    The template project generates the LICENSES folder that contains multiple
    licenses. This function will clear that folder up and move the chosen
    license to the generated project as the "LICENSE" file.
    """
    project_directory = os.path.realpath(os.path.curdir)
    license_file = os.path.join(project_directory, 'LICENSES',
                                '{{ cookiecutter.project_license }}')

    if not os.path.exists(license_file):
        raise IOError(
            'No known license for {{ cookiecutter.project_license }}')

    shutil.move(license_file, os.path.join(project_directory, 'LICENSE'))
    shutil.rmtree(os.path.join(project_directory, 'LICENSES'))


if __name__ == '__main__':
    set_license()
