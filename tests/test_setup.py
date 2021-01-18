from . import bake_cookie, subprocess_in_dir


def test_bake_and_run_tests(cookies):
    with bake_cookie(cookies) as result:
        assert result.project.isdir()
        subprocess_in_dir("python setup.py test", str(result.project)) == 0
        print("python setup.py test", str(result.project))
