import _ast

from peon.src.project.file.function_def.expression.returned_expr import ReturnedExpression
from peon.src.project.file.function_def.function import FunctionLint, FunctionParseResult


class ReturnedValueFixture:
    node_is_none = None
    assign_expression_as_input = _ast.Assign(lineno=1)
    pass_expression_as_input = _ast.Pass(lineno=1)
    plain_expression_as_input = _ast.Expr(lineno=1)
    function_body_is_empty = _ast.FunctionDef(lineno=1, body=[])
    function_body_without_return_expression = _ast.FunctionDef(
        lineno=1, body=[_ast.Pass(), _ast.Expr(), _ast.Assign],
    )
    function_body_with_return_expression = _ast.FunctionDef(
        lineno=1, body=[_ast.Pass(), _ast.Expr(), _ast.Assign(), _ast.Return(lineno=1, value=None)],
    )


class ResultReturnValueFixture:
    none = FunctionParseResult(
        return_not_none=bool(FunctionLint.EMPTY_RETURNED_VALUE),
        line_number=-1,
    ).__dict__
    wrong = FunctionParseResult(
        return_not_none=bool(FunctionLint.EMPTY_RETURNED_VALUE),
        line_number=1,
    ).__dict__
    success = FunctionParseResult(
        return_not_none=ReturnedExpression(_ast.Return(lineno=1, value=None)).value_not_none(),
        line_number=_ast.Return(lineno=1, value=None).lineno,
    ).__dict__


def test_node_is_none():
    assert FunctionLint(
        definition=ReturnedValueFixture.node_is_none,
    ).returned_value().__dict__ == ResultReturnValueFixture.none


def test_assign_expression_as_input():
    assert FunctionLint(
        definition=ReturnedValueFixture.assign_expression_as_input,
    ).returned_value().__dict__ == ResultReturnValueFixture.wrong


def test_pass_expression_as_input():
    assert FunctionLint(
        definition=ReturnedValueFixture.pass_expression_as_input,
    ).returned_value().__dict__ == ResultReturnValueFixture.wrong


def test_plain_expression_as_input():
    assert FunctionLint(
        definition=ReturnedValueFixture.plain_expression_as_input,
    ).returned_value().__dict__ == ResultReturnValueFixture.wrong


def test_function_body_is_empty():
    assert FunctionLint(
        definition=ReturnedValueFixture.function_body_is_empty,
    ).returned_value().__dict__ == ResultReturnValueFixture.wrong


def test_function_body_without_return_expression():
    assert FunctionLint(
        definition=ReturnedValueFixture.function_body_without_return_expression,
    ).returned_value().__dict__ == ResultReturnValueFixture.wrong


def test_function_body_with_return_expression():
    assert FunctionLint(
        definition=ReturnedValueFixture.function_body_with_return_expression,
    ).returned_value().__dict__ == ResultReturnValueFixture.success
