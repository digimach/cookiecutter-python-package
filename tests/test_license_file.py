"""
License file testing module for the generated project.
"""
import datetime
import os
from . import bake_cookie, load_cookiecutter_json


def test_license_file_exists(cookies):
    "Check that the LICENSE file exists"
    with bake_cookie(cookies) as result:
        license_file_path = result.project.join('LICENSE')
        assert os.path.exists(license_file_path)


def test_licenses_dir_not_present(cookies):
    "Check that the LICENSES dir is removed"
    with bake_cookie(cookies) as result:
        licenses_dir_path = result.project.join('LICENSES')
        assert not os.path.exists(licenses_dir_path)


def test_bake_selecting_license(cookies):
    """
    Test all licenses that the project can generate and make sure they contain
    known strings.
    """
    supported_licenses = load_cookiecutter_json()['project_license']
    now = datetime.datetime.now()

    for license in supported_licenses:
        with bake_cookie(cookies, extra_context={'project_license':
                                                 license}) as result:
            if license == 'Proprietary':
                assert "All rights reserved." in result.project.join(
                    'LICENSE').readlines()[1]
            else:
                assert license in result.project.join('LICENSE').readlines()[0]

            assert license in result.project.join('setup.py').read()

            license_file = result.project.join('LICENSE').read()
            assert str("Cookie Baker") in license_file
            assert str("baker@cookier.com") in license_file
            assert str(now.year) in license_file
