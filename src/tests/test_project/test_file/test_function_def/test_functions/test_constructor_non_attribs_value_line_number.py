import _ast

from peon.project.file.function_def.function import Function


def test_definitions_is_none():
    assert Function(definition=None).constructor_non_attribs_value_line_number() == ()


def test_definitions_is_not_a_function():
    assert Function(definition=_ast.Pass).constructor_non_attribs_value_line_number() == ()


def test_definitions_is_not_a_constructor():
    assert Function(
        definition=_ast.FunctionDef(name='test', body=[_ast.Expr(lineno=1)]),
    ).constructor_non_attribs_value_line_number() == ()


def test_definitions_consist_of_assign_with_attribute():
    assert Function(
        definition=_ast.FunctionDef(name='__init__', body=[_ast.Assign(targets=[_ast.Attribute(lineno=2)], lineno=1)]),
    ).constructor_non_attribs_value_line_number() == ()


def test_definitions_consist_of_assign_without_attribute():
    assert Function(
        definition=_ast.FunctionDef(name='__init__', body=[_ast.Assign(targets=[_ast.Expr(lineno=2)], lineno=1)]),
    ).constructor_non_attribs_value_line_number() == (2,)


def test_definitions_consist_of_any_but_not_a_assign():
    assert Function(
        definition=_ast.FunctionDef(name='__init__', body=[_ast.Pass(lineno=3)]),
    ).constructor_non_attribs_value_line_number() == (3,)
