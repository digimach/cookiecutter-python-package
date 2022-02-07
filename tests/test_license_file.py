"""
License file testing module for the generated project.
"""
import datetime
import os
from . import bake_cookie, load_cookiecutter_json


def test_license_file_exists(cookies):
    "Check that the LICENSE file exists"
    with bake_cookie(cookies) as result:
        license_file_path = result.project_path.joinpath("LICENSE.rst")
        assert os.path.exists(license_file_path)


def test_licenses_dir_not_present(cookies):
    "Check that the LICENSES dir is removed"
    with bake_cookie(cookies) as result:
        licenses_dir_path = result.project_path.joinpath("LICENSES")
        assert not os.path.exists(licenses_dir_path)


def test_bake_selecting_license(cookies):
    """
    Test all licenses that the project can generate and make sure they contain
    known strings.
    """
    supported_licenses = load_cookiecutter_json()["project_license"]
    now = datetime.datetime.now()

    for license in supported_licenses:
        with bake_cookie(cookies, extra_context={"project_license": license}) as result:
            license_file_path = result.project_path.joinpath("LICENSE.rst")

            with open(license_file_path, "r") as fp:
                license_file = fp.read()
                license_file_lines = license_file.splitlines()

            if license == "Proprietary":
                assert "All rights reserved." in license_file_lines[3]
            else:
                assert license in license_file_lines[2]

            assert (
                f"license = {license}"
                in result.project_path.joinpath("setup.cfg").read_text()
            )

            assert str("Cookie Baker") in license_file
            assert str("baker@cookier.com") in license_file
            assert str(now.year) in license_file
