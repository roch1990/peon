import _ast

from peon.src.project.file.function_def.function import Function


class ConstructorMutableAttribsLineNumberFixture:
    definition_is_none = None
    definition_is_not_a_function = _ast.Pass
    constructor_with_empty_body = _ast.FunctionDef(name='__init__', body=[])
    constructor_with_immutable = _ast.FunctionDef(
        name='__init__', body=[
            _ast.Assign(lineno=1, value=_ast.Tuple(elts=[1, 2, 3])),
            _ast.Assign(lineno=2, value=_ast.Str(s='a')),
            _ast.Assign(lineno=3, value=_ast.JoinedStr(values=None)),
        ],
    )
    constructor_with_mutable = _ast.FunctionDef(
        name='__init__', body=[
            _ast.Assign(lineno=1, value=_ast.List(elts=[1, 2, 3])),
            _ast.Assign(lineno=2, value=_ast.Set(elts=[1, 2, 3])),
            _ast.Assign(lineno=3, value=_ast.Dict(keys=['a'])),
        ],
    )


def test_definitions_is_none():
    assert Function(
        definition=ConstructorMutableAttribsLineNumberFixture.definition_is_none,
    ).constructor_mutable_attribs_line_number() == ()


def test_definition_is_not_a_function():
    assert Function(
        definition=ConstructorMutableAttribsLineNumberFixture.definition_is_not_a_function,
    ).constructor_mutable_attribs_line_number() == ()


def test_constructor_with_empty_body():
    assert Function(
        definition=ConstructorMutableAttribsLineNumberFixture.constructor_with_empty_body,
    ).constructor_mutable_attribs_line_number() == ()


def test_constructor_with_immutable():
    assert Function(
        definition=ConstructorMutableAttribsLineNumberFixture.constructor_with_immutable,
    ).constructor_mutable_attribs_line_number() == ()


def test_constructor_with_mutable():
    assert Function(
        definition=ConstructorMutableAttribsLineNumberFixture.constructor_with_mutable,
    ).constructor_mutable_attribs_line_number() == (1, 2, 3)
