import _ast

from peon.project.file.function_def.expression.returned_expr import ReturnedExpression
from peon.project.file.function_def.function import Function, FunctionParseResult


def test_node_is_none():
    assert Function(definition=None).returned_value().__dict__ == FunctionParseResult(
        return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
        line_number=-1,
    ).__dict__


def test_assign_expression_as_input():
    assert Function(definition=_ast.Assign(lineno=1)).returned_value().__dict__ == FunctionParseResult(
        return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
        line_number=1,
    ).__dict__


def test_pass_expression_as_input():
    assert Function(definition=_ast.Pass(lineno=1)).returned_value().__dict__ == FunctionParseResult(
        return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
        line_number=1,
    ).__dict__


def test_plain_expression_as_input():
    assert Function(definition=_ast.Expr(lineno=1)).returned_value().__dict__ == FunctionParseResult(
        return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
        line_number=1,
    ).__dict__


def test_function_body_is_empty():
    assert Function(definition=_ast.FunctionDef(lineno=1, body=[])).returned_value().__dict__ == FunctionParseResult(
        return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
        line_number=1,
    ).__dict__


def test_function_body_without_return_expression():
    assert Function(
        definition=_ast.FunctionDef(
            lineno=1, body=[_ast.Pass(), _ast.Expr(), _ast.Assign],
        ),
    ).returned_value().__dict__ == FunctionParseResult(
        return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
        line_number=1,
    ).__dict__


def test_function_body_with_return_expression():
    assert Function(
        definition=_ast.FunctionDef(
            lineno=1, body=[_ast.Pass(), _ast.Expr(), _ast.Assign(), _ast.Return(lineno=1, value=None)],
        ),
    ).returned_value().__dict__ == FunctionParseResult(
        return_not_none=ReturnedExpression(_ast.Return(lineno=1, value=None)).value_not_none(),
        line_number=_ast.Return(lineno=1, value=None).lineno,
    ).__dict__
