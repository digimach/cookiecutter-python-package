from . import bake_cookie, subprocess_in_dir


def test_doc_tox_env(cookies):
    with bake_cookie(cookies) as result:
        assert result.project_path.is_dir()
        subprocess_in_dir(
            "tox -e docs --workdir .tox",
            str(result.project_path),
        ) == 0
