"""
README.md file testing module for the generated project.
"""
import os
from . import bake_cookie


def test_readme_file_exists(cookies):
    "Test that the README.md file exists"
    with bake_cookie(cookies) as result:
        readme_file_path = result.project.join('README.md')
        assert os.path.exists(readme_file_path)
