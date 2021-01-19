from . import bake_cookie, subprocess_in_dir


def test_doc_generation(cookies):
    with bake_cookie(cookies) as result:
        assert result.project.isdir()
        subprocess_in_dir(
            'make --directory=./docs SPHINXOPTS="-W -n --keep-going" html',
            str(result.project),
        ) == 0


def test_doc_links(cookies):
    with bake_cookie(cookies) as result:
        assert result.project.isdir()
        subprocess_in_dir("make --directory=./docs linkcheck", str(result.project)) == 0
