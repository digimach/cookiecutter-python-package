"""
Test related to Git repo in the generated project.
"""
import git
import pytest

from . import bake_cookie


def test_git_repo_is_clean(cookies):
    "Check that Git repo does not have any files not committed"
    with bake_cookie(cookies) as result:
        assert result.project_path.is_dir()
        repo = git.Repo(result.project_path)
        assert not repo.bare
        assert not repo.is_dirty(untracked_files=True)


def test_no_git_repo(cookies):
    "Check that Git repo is not created when the option is False"
    with bake_cookie(cookies, extra_context={"initialize_git_repo": "no"}) as result:
        print(dir(result.project_path))
        assert result.project_path.is_dir()
        with pytest.raises(git.exc.InvalidGitRepositoryError):
            git.Repo(result.project_path)
