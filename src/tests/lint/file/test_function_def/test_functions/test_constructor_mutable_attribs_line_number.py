import _ast

from peon.project.file.function_def.function import Function


def test_definitions_is_none():
    assert Function(definition=None).constructor_mutable_attribs_line_number() == ()


def test_definition_is_not_a_function():
    assert Function(definition=_ast.Pass).constructor_mutable_attribs_line_number() == ()


def test_constructor_with_empty_body():
    assert Function(
        definition=_ast.FunctionDef(name='__init__', body=[]),
    ).constructor_mutable_attribs_line_number() == ()


def test_constructor_with_immutable():
    assert Function(
        _ast.FunctionDef(
            name='__init__', body=[
                _ast.Assign(lineno=1, value=_ast.Tuple(elts=[1, 2, 3])),
                _ast.Assign(lineno=2, value=_ast.Str(s='a')),
                _ast.Assign(lineno=3, value=_ast.JoinedStr(values=None)),
            ],
        ),
    ).constructor_mutable_attribs_line_number() == ()


def test_constructor_with_mutable():
    assert Function(
        _ast.FunctionDef(
            name='__init__', body=[
                _ast.Assign(lineno=1, value=_ast.List(elts=[1, 2, 3])),
                _ast.Assign(lineno=2, value=_ast.Set(elts=[1, 2, 3])),
                _ast.Assign(lineno=3, value=_ast.Dict(keys=['a'])),
            ],
        ),
    ).constructor_mutable_attribs_line_number() == (1, 2, 3)
