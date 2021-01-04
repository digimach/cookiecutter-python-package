#!/bin/env python3
"""
Cookiecutter post generation hook script that handles operations after the
template project is used to generate a target project.
"""

import shutil
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def initialize_git_repo():
    """
    Do a Git init and do a first commit in the generated project.
    We use git package installed on the target machine vs the gitpython module
    since that requires the package to be installed on the target machine.
    """
    subprocess.check_output("git init",
                            stderr=subprocess.STDOUT,
                            shell=True,
                            cwd=PROJECT_DIRECTORY)

    subprocess.check_output("git add --all",
                            stderr=subprocess.STDOUT,
                            shell=True,
                            cwd=PROJECT_DIRECTORY)

    commit_message = ("Initial commit - Generated project from cookiecutter"
                      " template.\n\n"
                      "Template created from"
                      " https://github.com/Digimach/cookiecutter-python-"
                      "package")

    author_info = "{{ cookiecutter.project_author_name }}"
    author_info += " <{{cookiecutter.project_author_email }}>"

    env = os.environ.copy()
    env['GIT_COMMITTER_NAME'] = "{{ cookiecutter.project_author_name }}"
    env['GIT_COMMITTER_EMAIL'] = "{{ cookiecutter.project_author_email }}"

    try:
        subprocess.check_output((f'git commit --author "{author_info}"'
                                 f' --message "{commit_message}"'),
                                shell=True,
                                cwd=PROJECT_DIRECTORY,
                                env=env)
    except subprocess.CalledProcessError as exc_info:
        if exc_info.returncode != 0:
            print(exc_info.output)
        raise


def set_license():
    """
    The template project generates the LICENSES folder that contains multiple
    licenses. This function will clear that folder up and move the chosen
    license to the generated project as the "LICENSE" file.
    """
    project_directory = PROJECT_DIRECTORY
    license_file = os.path.join(project_directory, 'LICENSES',
                                '{{ cookiecutter.project_license }}')

    if not os.path.exists(license_file):
        raise IOError(
            'No known license for {{ cookiecutter.project_license }}')

    shutil.move(license_file, os.path.join(project_directory, 'LICENSE'))
    shutil.rmtree(os.path.join(project_directory, 'LICENSES'))


if __name__ == '__main__':
    set_license()

    if '{{ cookiecutter.initialize_git_repo|lower }}' == 'yes':
        initialize_git_repo()
