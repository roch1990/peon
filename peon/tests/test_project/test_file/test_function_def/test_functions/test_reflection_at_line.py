import _ast

from peon.src.project.file.function_def.function import Function


class ReflectionAtLineFixture:
    empty_node = _ast.Pass
    is_instance_at_first_lvl = _ast.FunctionDef(id='isinstance', lineno=1)
    type_at_first_lvl = _ast.FunctionDef(id='type', lineno=1)
    is_instance_at_second_lvl = _ast.FunctionDef(body=[_ast.Expr(id='isinstance', lineno=2)], lineno=1)
    type_at_second_lvl = _ast.FunctionDef(body=[_ast.Expr(id='type', lineno=2)], lineno=1)


def test_empty_node():
    assert Function(
        definition=ReflectionAtLineFixture.empty_node,
    ).reflection_at_line() == tuple()


def test_is_instance_at_first_lvl():
    assert Function(
        definition=ReflectionAtLineFixture.is_instance_at_first_lvl,
    ).reflection_at_line() == (1,)


def test_type_at_first_lvl():
    assert Function(
        definition=ReflectionAtLineFixture.type_at_first_lvl,
    ).reflection_at_line() == (1,)


def test_is_instance_at_second_lvl():
    assert Function(
        definition=ReflectionAtLineFixture.is_instance_at_second_lvl,
    ).reflection_at_line() == (2,)


def test_type_at_second_lvl():
    assert Function(
        definition=ReflectionAtLineFixture.type_at_second_lvl,
    ).reflection_at_line() == (2,)
