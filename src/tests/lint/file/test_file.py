import pytest

from peon.lint.file.file import File
from tests.utils import TestFile


def test_name():
    assert File(body=TestFile().body, name='test').name == 'test'


def test_none_name():
    assert File(body=TestFile().body, name=None).name is None


def test_body():
    assert File(body=TestFile().body, name='test').body == TestFile().body


def test_none_body():
    with pytest.raises(TypeError):
        assert File(body=None, name='test').body is None


def test_class_statement():
    assert File(body=TestFile().body, name='test').class_statement[0].raw_line == 'class Abstracter:'


def test_def_statement():
    assert File(body=TestFile().body, name='test').func_statement[0].raw_line == 'def __init__(self, something: list):'


def test_return_statement():
    assert File(body=TestFile().body, name='test').return_statement[0].raw_line == 'return None'


def test_lines():
    assert File(body=TestFile().body, name='test').lines[0].raw_line == 'class Abstracter:'
    assert File(body=TestFile().body, name='test').lines[1].raw_line == 'def __init__(self, something: list):'
    assert File(body=TestFile().body, name='test').lines[2].raw_line == 'self.something = something'
    assert File(body=TestFile().body, name='test').lines[3].raw_line == 'return None'
