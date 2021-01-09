#!/bin/env python3
"""
Cookiecutter post generation hook script that handles operations after the
template project is used to generate a target project.
"""

import os
import shlex
import shutil
import subprocess
import sys
from collections import OrderedDict  # noqa pylint: disable=unused-import

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def initialize_git_repo():
    """
    Initialize the Git repository in the generated project.
    """
    subprocess.check_output("git init",
                            stderr=subprocess.STDOUT,
                            shell=True,
                            cwd=PROJECT_DIRECTORY)


def git_add():
    """
    Do a Git add operation on the generated project.
    """
    subprocess.check_output("git add --all",
                            stderr=subprocess.STDOUT,
                            shell=True,
                            cwd=PROJECT_DIRECTORY)


def git_commit():
    """
    Commit the staged changes in the generated project.
    """

    cookiecutter_config = {{cookiecutter}}  # noqa pylint: disable=undefined-variable

    cookiecutter_config_str = ""
    for key, val in cookiecutter_config.items():  # noqa pylint: disable=no-member
        cookiecutter_config_str += f"  {key}: {val}\n"

    commit_message = ("Template applied from"
                      " https://github.com/Digimach/cookiecutter-python-"
                      "package\n\n"
                      "Template configuration:\n"
                      f"{cookiecutter_config_str}")

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


def is_git_repo_clean():
    """
    Check to confirm if the Git repository is clean and has no uncommitted
    changes. If its clean return True otherwise False.
    """
    try:
        if sys.version_info.minor >= 7:
            git_status = subprocess.run(shlex.split('git status --porcelain'),
                                        capture_output=True,
                                        cwd=PROJECT_DIRECTORY,
                                        check=True)
        elif sys.version_info.minor < 7:
            git_status = subprocess.run(shlex.split('git status --porcelain'),
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        cwd=PROJECT_DIRECTORY,
                                        check=True)
    except subprocess.CalledProcessError:
        print(f"** Git repository in {PROJECT_DIRECTORY} cannot get status")
        sys.exit(1)

    if git_status.stdout == b'' and git_status.stderr == b'':
        return True

    return False


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
        if not is_git_repo_clean():
            git_add()
            git_commit()

    sys.exit(0)
