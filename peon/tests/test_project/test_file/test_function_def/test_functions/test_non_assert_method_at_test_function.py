import _ast

from peon.src.project.file.function_def.function import FunctionLint


class NonAssertMethodAtTestFunctionFixture:
    definition_is_none = None
    definitions_is_not_a_function = _ast.Pass()
    definitions_is_not_a_test_function = _ast.FunctionDef(name='not_a_test')
    definitions_with_only_assert = _ast.FunctionDef(name='test', body=[_ast.Assert()])
    definitions_with_code = _ast.FunctionDef(name='test', body=[_ast.Pass(lineno=1), _ast.Assert()])


def test_definitions_is_none():
    assert FunctionLint(
        definition=NonAssertMethodAtTestFunctionFixture.definition_is_none,
    ).non_assert_methods_at_test_function() == ()


def test_definitions_is_not_a_function():
    assert FunctionLint(
        definition=NonAssertMethodAtTestFunctionFixture.definitions_is_not_a_function,
    ).non_assert_methods_at_test_function() == ()


def test_definitions_is_not_a_test_function():
    assert FunctionLint(
        definition=NonAssertMethodAtTestFunctionFixture.definitions_is_not_a_test_function,
    ).non_assert_methods_at_test_function() == ()


def test_definitions_with_only_assert():
    assert FunctionLint(
        definition=NonAssertMethodAtTestFunctionFixture.definitions_with_only_assert,
    ).non_assert_methods_at_test_function() == ()


def test_definitions_with_code():
    assert FunctionLint(
        definition=NonAssertMethodAtTestFunctionFixture.definitions_with_code,
    ).non_assert_methods_at_test_function() == (1,)
