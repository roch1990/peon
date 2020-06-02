import _ast
import pytest

from peon.src.project.file.function_def.function import Function


class StaticOrPrivateFixture:
    definition_is_assign = _ast.Assign()
    definition_is_pass = _ast.Pass()
    definition_is_expr = _ast.Expr()
    empty_decorator_list_and_name = _ast.FunctionDef()
    empty_decorator_list = _ast.FunctionDef(name='test')
    is_private = _ast.FunctionDef(name='_test')
    is_protected = _ast.FunctionDef(name='__test')
    is_magic = _ast.FunctionDef(name='__test__')
    decorated = _ast.FunctionDef(name='test', decorator_list=['any_decorator'])
    is_static = _ast.FunctionDef(
        name='test', decorator_list=[_ast.FunctionDef(id='staticmethod')],
    )


def test_function_definition_is_assign():
    assert Function(
        definition=StaticOrPrivateFixture.definition_is_assign,
    ).static_or_private() is False


def test_function_definition_is_pass():
    assert Function(
        definition=StaticOrPrivateFixture.definition_is_pass,
    ).static_or_private() is False


def test_function_definition_is_expr():
    assert Function(
        definition=StaticOrPrivateFixture.definition_is_expr,
    ).static_or_private() is False


def test_empty_decorator_list_and_name():
    with pytest.raises(AttributeError):
        assert Function(
            definition=StaticOrPrivateFixture.empty_decorator_list_and_name,
        ).static_or_private()


def test_empty_decorator_list():
    assert Function(
        definition=StaticOrPrivateFixture.empty_decorator_list,
    ).static_or_private() is False


def test_method_is_private():
    assert Function(
        definition=StaticOrPrivateFixture.is_private,
    ).static_or_private() is True


def test_method_is_protected():
    assert Function(
        definition=StaticOrPrivateFixture.is_protected,
    ).static_or_private() is True


def test_method_is_magic():
    assert Function(
        definition=StaticOrPrivateFixture.is_magic,
    ).static_or_private() is False


def test_method_decorated():
    assert Function(
        definition=StaticOrPrivateFixture.decorated,
    ).static_or_private() is False


def test_method_is_static():
    assert Function(
        definition=StaticOrPrivateFixture.is_static,
    ).static_or_private() is True
