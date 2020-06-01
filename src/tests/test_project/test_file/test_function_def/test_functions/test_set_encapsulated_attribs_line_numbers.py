import _ast

from peon.project.file.function_def.function import Function


class SetEncapsulatedAttribsLineNumbersFixture:
    definition_is_none = None
    definition_is_pass = _ast.Pass()
    is_constructor = _ast.FunctionDef(name='__init__')
    without_assign = _ast.FunctionDef(name='test', body=[_ast.Pass()])
    with_assign_without_self = _ast.FunctionDef(
        name='test', body=[
            _ast.Pass(),
            _ast.Assign(targets=[_ast.Attribute(value=(_ast.Name(id='test')), lineno=1)]),
        ],
    )
    with_assign_with_self = _ast.FunctionDef(
        name='test', body=[
            _ast.Pass(),
            _ast.Assign(targets=[_ast.Attribute(value=(_ast.Name(id='self')), lineno=1)]),
        ],
    )



def test_function_definition_is_none():
    assert Function(
        definition=SetEncapsulatedAttribsLineNumbersFixture.definition_is_none,
    ).set_encapsulated_attribs_line_numbers() == ()


def test_function_definition_is_pass():
    assert Function(
        definition=SetEncapsulatedAttribsLineNumbersFixture.definition_is_pass,
    ).set_encapsulated_attribs_line_numbers() == ()


def test_function_is_constructor():
    assert Function(
        definition=SetEncapsulatedAttribsLineNumbersFixture.is_constructor,
    ).set_encapsulated_attribs_line_numbers() == ()


def test_function_without_assign():
    assert Function(
        definition=SetEncapsulatedAttribsLineNumbersFixture.without_assign,
    ).set_encapsulated_attribs_line_numbers() == ()


def test_function_with_assign_without_self():
    assert Function(
        definition=SetEncapsulatedAttribsLineNumbersFixture.with_assign_without_self,
    ).set_encapsulated_attribs_line_numbers() == ()


def test_function_with_assign_with_self():
    assert Function(
        definition=SetEncapsulatedAttribsLineNumbersFixture.with_assign_with_self,
    ).set_encapsulated_attribs_line_numbers() == (1,)
