import ast

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
    PYTHON_REFLECTION_EXPRESSIONS = ['type', 'isinstance']

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

        if isinstance(node, _ast.Assign):
            return FunctionParseResult(
                return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
                line_number=node.lineno,
            )
        elif isinstance(node, _ast.Pass):
            return FunctionParseResult(
                return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
                line_number=node.lineno,
            )

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

    def static_or_private(self):
        if isinstance(self.definition, _ast.Assign):
            return False
        elif isinstance(self.definition, _ast.Pass):
            return False

        decorators = self.definition.decorator_list
        for item in decorators:
            if item.id == 'staticmethod':
                return True
        if self.definition.name.startswith('_') or self.definition.name.startswith('__'):
            if not self.definition.name.endswith('__'):
                return True
        return False

    def name(self):
        return self.definition.name

    def reflection_at_line(self):

        reflection_list = []
        for node in ast.walk(self.definition):
            try:
                if node.id in self.PYTHON_REFLECTION_EXPRESSIONS:
                    reflection_list.append(node.lineno)
            except:
                continue
        return reflection_list
