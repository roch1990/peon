import pytest

from peon.lint.lint import Lint
from tests.utils import TestProjectTree


def test_sucess():
    assert Lint(TestProjectTree().project_tree.inspect()).project() is None


def test_none_path():
    with pytest.raises(TypeError):
        assert Lint(None).project()


def test_empty_project():
    assert Lint([]).project() is None
