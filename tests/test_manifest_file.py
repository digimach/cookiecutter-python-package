"""
Manifest file testing module for the generated project.
"""
import os

from . import bake_cookie, load_cookiecutter_json


def test_manifest_file(cookies):
    "Test that the MANIFEST.in file exists and the content is valid"
    with bake_cookie(cookies) as result:
        manifest_file_path = result.project.join("MANIFEST.in")

        assert os.path.exists(manifest_file_path)

        manifest_file = result.project.join("MANIFEST.in").read()
        cookiecutter_json = load_cookiecutter_json()

        assert str(cookiecutter_json["project_slug"]) in manifest_file
