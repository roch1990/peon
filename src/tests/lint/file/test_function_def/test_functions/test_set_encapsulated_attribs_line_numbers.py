import _ast

from peon.project.file.function_def.function import Function


def test_function_definition_is_none():
    assert Function(definition=None).set_encapsulated_attribs_line_numbers() == ()


def test_function_definition_is_pass():
    assert Function(_ast.Pass()).set_encapsulated_attribs_line_numbers() == ()


def test_function_is_constructor():
    assert Function(_ast.FunctionDef(name='__init__')).set_encapsulated_attribs_line_numbers() == ()


def test_function_without_assign():
    assert Function(_ast.FunctionDef(name='test', body=[_ast.Pass()])).set_encapsulated_attribs_line_numbers() == ()


def test_function_with_assign_without_self():
    assert Function(
        _ast.FunctionDef(
            name='test', body=[
                _ast.Pass(),
                _ast.Assign(targets=[_ast.Attribute(value=(_ast.Name(id='test')), lineno=1)]),
            ],
        ),
    ).set_encapsulated_attribs_line_numbers() == ()


def test_function_with_assign_with_self():
    assert Function(
        _ast.FunctionDef(
            name='test', body=[
                _ast.Pass(),
                _ast.Assign(targets=[_ast.Attribute(value=(_ast.Name(id='self')), lineno=1)]),
            ],
        ),
    ).set_encapsulated_attribs_line_numbers() == (1,)
