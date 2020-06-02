import pytest

from peon.comandline.project_tree import ProjectTree
from tests.utils import TestProjectTree


def test_inspect_success():
    assert list(
        set(
            ProjectTree(
                path_to_project=[f'{TestProjectTree().pythonpath}/tests/fixtures'],
            ).inspect(),
        ) - set([
                   f'{TestProjectTree().pythonpath}/tests/fixtures/dummy_code.py',
                   f'{TestProjectTree().pythonpath}/tests/fixtures/__init__.py',
                   f'{TestProjectTree().pythonpath}/tests/fixtures/dummy_folder/__init__.py',
        ]),
    ) == []


def test_inspect_type_error():
    with pytest.raises(TypeError):
        assert ProjectTree(None).inspect()


def test_inspect_wrong_path():
    assert ProjectTree(['atatat/tratata']).inspect() == []
