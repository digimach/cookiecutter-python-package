"""
Manifest file testing module for the generated project.
"""
import os

from . import bake_cookie, load_cookiecutter_json


def test_manifest_file(cookies):
    "Test that the MANIFEST.in file exists and the content is valid"
    with bake_cookie(cookies) as result:
        manifest_file_path = result.project_path.joinpath("MANIFEST.in")
        cookiecutter_json = load_cookiecutter_json()

        assert os.path.exists(manifest_file_path)

        with open(manifest_file_path, "r") as fp:
            assert str(cookiecutter_json["project_slug"]) in fp.read()
