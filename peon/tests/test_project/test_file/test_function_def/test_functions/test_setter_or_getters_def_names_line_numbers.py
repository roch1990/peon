import _ast

from peon.src.project.file.function_def.function import FunctionLint


class SetterOrGetterDefNamesLineNumbersFixture:
    definition_is_none = None
    definition_is_pass = _ast.Pass()
    name_is_none = _ast.FunctionDef(name=None)
    without_setget_keywords = _ast.FunctionDef(name='test')
    with_set_keywords = _ast.FunctionDef(name='set_test', lineno=1)
    with_get_keywords = _ast.FunctionDef(name='get_test', lineno=2)


def test_function_definition_is_none():
    assert FunctionLint(
        definition=SetterOrGetterDefNamesLineNumbersFixture.definition_is_none,
    ).setter_or_getters_def_names_line_numbers() == ()


def test_function_definition_is_pass():
    assert FunctionLint(
        definition=SetterOrGetterDefNamesLineNumbersFixture.definition_is_pass,
    ).setter_or_getters_def_names_line_numbers() == ()


def test_method_name_is_none():
    assert FunctionLint(
        definition=SetterOrGetterDefNamesLineNumbersFixture.name_is_none,
    ).setter_or_getters_def_names_line_numbers() == ()


def test_method_without_setget_keywords():
    assert FunctionLint(
        definition=SetterOrGetterDefNamesLineNumbersFixture.without_setget_keywords,
    ).setter_or_getters_def_names_line_numbers() == ()


def test_method_with_set_keywords():
    assert FunctionLint(
        definition=SetterOrGetterDefNamesLineNumbersFixture.with_set_keywords,
    ).setter_or_getters_def_names_line_numbers() == (1,)


def test_method_with_get_keywords():
    assert FunctionLint(
        definition=SetterOrGetterDefNamesLineNumbersFixture.with_get_keywords,
    ).setter_or_getters_def_names_line_numbers() == (2,)
