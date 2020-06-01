import _ast

from peon.project.file.function_def.function import Function


class ConstructorNonAttribsValueLineNumberFixture:
    definition_is_none = None
    definition__is_not_a_function = _ast.Pass
    definitions_is_not_a_constructor = _ast.FunctionDef(name='test', body=[_ast.Expr(lineno=1)])
    definitions_consist_of_assign_with_attribute = _ast.FunctionDef(
        name='__init__', body=[_ast.Assign(targets=[_ast.Attribute(lineno=2)], lineno=1)],
    )
    definitions_consist_of_assign_without_attribute = _ast.FunctionDef(
        name='__init__', body=[_ast.Assign(targets=[_ast.Attribute(lineno=2)], lineno=1)],
    )
    definitions_consist_of_any_but_not_a_assign = _ast.FunctionDef(name='__init__', body=[_ast.Pass(lineno=3)])


def test_definitions_is_none():
    assert Function(
        definition=ConstructorNonAttribsValueLineNumberFixture.definition_is_none,
    ).constructor_non_attribs_value_line_number() == ()


def test_definitions_is_not_a_function():
    assert Function(
        definition=ConstructorNonAttribsValueLineNumberFixture.definition__is_not_a_function,
    ).constructor_non_attribs_value_line_number() == ()


def test_definitions_is_not_a_constructor():
    assert Function(
        definition=ConstructorNonAttribsValueLineNumberFixture.definitions_is_not_a_constructor,
    ).constructor_non_attribs_value_line_number() == ()


def test_definitions_consist_of_assign_with_attribute():
    assert Function(
        definition=ConstructorNonAttribsValueLineNumberFixture.definitions_consist_of_assign_with_attribute,
    ).constructor_non_attribs_value_line_number() == ()


def test_definitions_consist_of_assign_without_attribute():
    assert Function(
        definition=ConstructorNonAttribsValueLineNumberFixture.definitions_consist_of_assign_without_attribute,
    ).constructor_non_attribs_value_line_number() == (2,)


def test_definitions_consist_of_any_but_not_a_assign():
    assert Function(
        definition=ConstructorNonAttribsValueLineNumberFixture.definitions_consist_of_any_but_not_a_assign,
    ).constructor_non_attribs_value_line_number() == (3,)
