import _ast

from peon.lint.file.function_def.expression.returned_expr import ReturnedExpression


class FunctionParseResult:

    def __init__(
            self,
            return_not_none: bool,
            line_number: int,
    ):
        self.return_not_none = return_not_none
        self.line_number = line_number


class Function:
    """
    class for function processing
    """

    EMPTY_RETURNED_VALUE = True

    def __init__(
            self,
            definition: _ast.FunctionDef,
    ):
        self.definition = definition

    def returned_value(self) -> FunctionParseResult:
        """
        return value of function "return" expression
        :return:
        """

        node = self.definition

        for item in node.body:
            if isinstance(item, _ast.Return):
                return FunctionParseResult(
                    return_not_none=ReturnedExpression(item).value_not_none(),
                    line_number=item.lineno,
                )
        return FunctionParseResult(
            return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
            line_number=node.lineno,
        )

    def static(self):
        decorators = self.definition.decorator_list
        for item in decorators:
            if item.id == 'staticmethod':
                return True
        return False
