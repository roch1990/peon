import _ast

from peon.project.file.function_def.function import Function


def test_function_definition_is_none():
    assert Function(definition=None).setter_or_getters_def_names_line_numbers() == ()


def test_function_definition_is_pass():
    assert Function(_ast.Pass()).setter_or_getters_def_names_line_numbers() == ()


def test_method_name_is_none():
    assert Function(_ast.FunctionDef(name=None)).setter_or_getters_def_names_line_numbers() == ()


def test_method_without_setget_keywords():
    assert Function(_ast.FunctionDef(name='test')).setter_or_getters_def_names_line_numbers() == ()


def test_method_with_set_keywords():
    assert Function(_ast.FunctionDef(name='set_test', lineno=1)).setter_or_getters_def_names_line_numbers() == (1,)


def test_method_with_get_keywords():
    assert Function(_ast.FunctionDef(name='get_test', lineno=2)).setter_or_getters_def_names_line_numbers() == (2,)
