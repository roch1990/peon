import _ast

from peon.project.file.function_def.function import Function


def test_empty_node():
    assert Function(_ast.Pass).reflection_at_line() == tuple()


def test_is_instance_at_first_lvl():
    assert Function(_ast.FunctionDef(id='isinstance', lineno=1)).reflection_at_line() == (1,)


def test_type_at_first_lvl():
    assert Function(_ast.FunctionDef(id='type', lineno=1)).reflection_at_line() == (1,)


def test_is_instance_at_second_lvl():
    assert Function(
        _ast.FunctionDef(body=[_ast.Expr(id='isinstance', lineno=2)], lineno=1),
    ).reflection_at_line() == (2,)


def test_type_at_second_lvl():
    assert Function(_ast.FunctionDef(body=[_ast.Expr(id='type', lineno=2)], lineno=1)).reflection_at_line() == (2,)
