import _ast
import pytest

from peon.project.file.function_def.function import Function


def test_function_definition_is_assign():
    assert Function(_ast.Assign()).static_or_private() is False


def test_function_definition_is_pass():
    assert Function(_ast.Pass()).static_or_private() is False


def test_function_definition_is_expr():
    assert Function(_ast.Expr()).static_or_private() is False


def test_empty_decorator_list_and_name():
    with pytest.raises(AttributeError):
        assert Function(_ast.FunctionDef()).static_or_private()


def test_empty_decorator_list():
    assert Function(_ast.FunctionDef(name='test')).static_or_private() is False


def test_method_is_private():
    assert Function(_ast.FunctionDef(name='_test')).static_or_private() is True


def test_method_is_protected():
    assert Function(_ast.FunctionDef(name='__test')).static_or_private() is True


def test_method_is_magic():
    assert Function(_ast.FunctionDef(name='__test__')).static_or_private() is False


def test_method_decorated():
    assert Function(_ast.FunctionDef(name='test', decorator_list=['any_decorator'])).static_or_private() is False


def test_method_is_static():
    assert Function(_ast.FunctionDef(name='test', decorator_list=['staticmethod'])).static_or_private() is False
