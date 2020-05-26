import _ast

from peon.project.file.function_def.function import Function


def test_definitions_is_none():
    assert Function(definition=None).non_assert_methods_at_test_function() == ()


def test_definitions_is_not_a_function():
    assert Function(definition=_ast.Pass()).non_assert_methods_at_test_function() == ()


def test_definitions_is_not_a_test_function():
    assert Function(definition=_ast.FunctionDef(name='not_a_test')).non_assert_methods_at_test_function() == ()


def test_definitions_with_only_assert():
    assert Function(
        definition=_ast.FunctionDef(name='test', body=[_ast.Assert()]),
    ).non_assert_methods_at_test_function() == ()


def test_definitions_with_code():
    assert Function(
        definition=_ast.FunctionDef(name='test', body=[_ast.Pass(lineno=1), _ast.Assert()]),
    ).non_assert_methods_at_test_function() == (1,)
