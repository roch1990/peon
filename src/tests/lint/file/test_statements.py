import pytest

from peon.lint.file.statements import Statements
from tests.utils import TestFile


def test_constants():
    assert Statements.CLASS_STATEMENT == 'class'
    assert Statements.FUNC_STATEMENT == 'def'
    assert Statements.RETURN_STATEMENT == 'return'
    assert Statements.ALL_LINES is None


def test_class_check():
    assert Statements(statement='class', text=TestFile().body).check()[0].raw_line == 'class Abstracter:'


def test_func_check():
    assert Statements(statement='def', text=TestFile().body).check()[0].raw_line == 'def __init__(self, something: list):'


def test_return_check():
    assert Statements(statement='return', text=TestFile().body).check()[0].raw_line == 'return None'


def test_lines():
    assert Statements(statement='', text=TestFile().body).check() == ()


def test_all_lines_check():
    assert Statements(statement=Statements.ALL_LINES, text=TestFile().body).check()[0].raw_line == 'class Abstracter:'
    assert Statements(statement=Statements.ALL_LINES, text=TestFile().body).check()[1].raw_line == 'def __init__(self, something: list):'
    assert Statements(statement=Statements.ALL_LINES, text=TestFile().body).check()[2].raw_line == 'self.something = something'
    assert Statements(statement=Statements.ALL_LINES, text=TestFile().body).check()[3].raw_line == 'return None'


def test_none_statement():
    assert Statements(statement=None, text=TestFile().body).check()[0].raw_line == 'class Abstracter:'
    assert Statements(statement=None, text=TestFile().body).check()[1].raw_line == 'def __init__(self, something: list):'
    assert Statements(statement=None, text=TestFile().body).check()[2].raw_line == 'self.something = something'
    assert Statements(statement=None, text=TestFile().body).check()[3].raw_line == 'return None'


def test_none_file_check():
    with pytest.raises(TypeError):
        assert Statements(statement='class', text=None).check()[0].raw_line == 'class Abstracter:'

