"""
CODE_OF_CONDUCT file testing module for the generated project.
"""
import os
from . import bake_cookie, load_cookiecutter_json


def test_code_of_conduct_file(cookies):
    "Test that the CODE_OF_CONDUCT.md file exists and the content is valid"
    with bake_cookie(cookies) as result:
        code_of_conduct_path = result.project.join('CODE_OF_CONDUCT.rst')

        assert os.path.exists(code_of_conduct_path)

        code_of_conduct = result.project.join('CODE_OF_CONDUCT.rst').read()
        cookiecutter_json = load_cookiecutter_json()

        assert str(
            cookiecutter_json['project_author_email']) in code_of_conduct
