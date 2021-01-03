"""
Common modules, functions, pytest fixtures and contextmanager are placed
in this module that can be used by submodules.
"""
import json
import os
import shlex
import subprocess
from contextlib import contextmanager


@contextmanager
def bake_cookie(cookies, *args, **kwargs):
    """
    Bake the cookiecutter project with some test context.

    :param cookies: pytest_cookies.Cookies
    :param (): All other positional args will be passed to cookies.bake call.
    :param (kwargs): All keyword arguments will be passed to cookies.bake call,
        Caller can overide or add additional context by passing in extra_context
            kwarg.
    """
    extra_context = {
        'project_slug': 'baked_cookie',
        'project_author_name': 'Cookie Baker',
        'project_author_email': 'baker@cookier.com'
    }

    if 'extra_context' not in kwargs.keys():
        kwargs['extra_context'] = extra_context
    elif not isinstance(kwargs['extra_context'], dict):
        raise TypeError('extra_context has to be a type of "dict"')
    else:
        kwargs['extra_context'].update(extra_context)

    result = cookies.bake(*args, **kwargs)

    try:
        yield result
    finally:
        print(result)


@contextmanager
def in_dir(dir_path):
    """
    Switch context of the directory to execute code within that directory and
    switch out to the caller's current directory upon completion.

    :param dir_path: The path to chdir into and yield
    """
    current_path = os.getcwd()
    try:
        os.chdir(dir_path)
        yield
    finally:
        os.chdir(current_path)


def subprocess_in_dir(command, dirpath=None):
    """
    Run a command via subprocess from inside a given directory and checking
    the return code. Will raise an exception if the exit code is not zero.
    :param command: Command that will be passed to subprocess.check_call. The
        command will be passed on to subprocess.check_call after being processed
        by shlex.split.
    :param dirpath: String, path of the directory the command is being run.
        Default: None, if None, the current directory will be used.
    """
    if dirpath is None:
        dirpath = os.getcwd()

    with in_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def load_cookiecutter_json():
    """
    Load the cookiecutter.json file and return it as dict
    """
    cookiecutter_json_file_path = os.path.join(os.path.dirname(__file__),
                                               os.pardir, 'cookiecutter.json')
    with open(cookiecutter_json_file_path) as fp:
        data = json.load(fp)

    return data
