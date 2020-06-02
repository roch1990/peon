import pytest
from peon.tests.utils import TestProjectTree

from peon.src.lint.lint import Lint


def test_sucess():
    assert Lint(TestProjectTree().project_tree.inspect()).project() is None


def test_none_path():
    with pytest.raises(TypeError):
        assert Lint(None).project()


def test_empty_project():
    assert Lint([]).project() is None
