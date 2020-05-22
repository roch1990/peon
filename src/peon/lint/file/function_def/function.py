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
    PYTHON_REFLECTION_EXPRESSIONS = ('type', 'isinstance')
    MUTABLE_TYPES = ('set', 'dict', 'list')

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

    def constructor_non_attribs_value_line_number(self):

        line_numbers = []
        if not isinstance(self.definition, _ast.FunctionDef):
            return line_numbers

        if self.definition.name == '__init__':
            for expressions in self.definition.body:
                if not isinstance(expressions, _ast.Assign):
                    line_numbers.append(expressions.lineno)
                    continue

                for target in expressions.targets:
                    if not isinstance(target, _ast.Attribute):
                        line_numbers.append(target.lineno)

        return line_numbers

    def non_assert_methods_at_test_function(self):

        line_numbers = []
        if not isinstance(self.definition, _ast.FunctionDef):
            return line_numbers

        if self.definition.name.startswith('test'):
            for expressions in self.definition.body:
                if not isinstance(expressions, _ast.Assert):
                    line_numbers.append(expressions.lineno)

        return line_numbers

    def constructor_mutable_attribs_line_number(self):

        line_numbers = []
        if not isinstance(self.definition, _ast.FunctionDef):
            return line_numbers

        if self.definition.name == '__init__':
            for expressions in self.definition.body:
                # list
                if expressions.value.__dict__.get('elts') is not None:
                    line_numbers.append(expressions.lineno)
                # dict
                elif expressions.value.__dict__.get('keys') is not None:
                    line_numbers.append(expressions.lineno)
                # via keywords (list(), dict(), set())
                elif expressions.value.__dict__.get('func') is not None:
                    if expressions.value\
                            .__dict__.get('func')\
                            .__dict__.get('id') \
                            in self.MUTABLE_TYPES:
                        line_numbers.append(expressions.lineno)

        return line_numbers
