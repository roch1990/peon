import ast
from typing import Tuple

import _ast

from peon.project.file.function_def.expression.returned_expr import ReturnedExpression


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
    Class for handling in-code inspected methods definitions
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
        :return: FunctionParseResult object
        """

        node = self.definition
        # if function does not has body
        if not node:
            return FunctionParseResult(
                return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
                line_number=node.lineno,
            )

        # skip plain assignment expressions
        if isinstance(node, _ast.Assign):
            return FunctionParseResult(
                return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
                line_number=node.lineno,
            )
        # skip plain pass expressions
        elif isinstance(node, _ast.Pass):
            return FunctionParseResult(
                return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
                line_number=node.lineno,
            )
        # skip for any other plain expressions
        elif isinstance(node, _ast.Expr):
            return FunctionParseResult(
                return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
                line_number=node.lineno,
            )
        # iterate over function body
        for item in node.body:
            # check, that expression has return type
            if isinstance(item, _ast.Return):
                return FunctionParseResult(
                    return_not_none=ReturnedExpression(item).value_not_none(),
                    line_number=item.lineno,
                )
        # in any other case - return empty
        return FunctionParseResult(
            return_not_none=bool(Function.EMPTY_RETURNED_VALUE),
            line_number=node.lineno,
        )

    def static_or_private(self) -> bool:
        """
        Check method for 'static' or 'private' statements
        :return: bool
        """
        # skip plain assignments
        if isinstance(self.definition, _ast.Assign):
            return False
        # skip plain pass expressions
        elif isinstance(self.definition, _ast.Pass):
            return False
        # skip plain expressions
        elif isinstance(self.definition, _ast.Expr):
            return False

        # get list of method decorators
        decorators = self.definition.decorator_list
        # iterate over decorators
        for item in decorators:
            # if 'staticmethod' in decorator list
            if item.id == 'staticmethod':
                return True
        # check for '_' and '__' starts chars
        if self.definition.name.startswith('_') or self.definition.name.startswith('__'):
            # skip magic methods
            if not self.definition.name.endswith('__'):
                return True
        return False

    def name(self) -> str:
        """
        Strange method for fun. Yes, looks like a getter.
        :return:
        """
        return self.definition.name

    def reflection_at_line(self) -> Tuple[int]:
        """
        Check method for 'isinstance' and 'type' expressions
        :return: list of line numbers, where was found that expressions
        """
        reflection_list = []
        # iterate over all subnodes in node
        for node in ast.walk(self.definition):
            # some subnodes does not has id attribute
            try:
                # append if node.id is 'isinstance' or 'type'
                if node.id in self.PYTHON_REFLECTION_EXPRESSIONS:
                    line_number: int = node.lineno
                    reflection_list.append(line_number)
            except:
                # skip if node.id is not exist
                continue
        # dont forget to convert to immutable type
        return tuple(reflection_list)

    def constructor_non_attribs_value_line_number(self) -> Tuple[int]:

        line_numbers = []
        if not isinstance(self.definition, _ast.FunctionDef):
            return tuple(line_numbers)

        if self.definition.name == '__init__':
            for expressions in self.definition.body:
                if not isinstance(expressions, _ast.Assign):
                    line_numbers.append(expressions.lineno)
                    continue

                for target in expressions.targets:
                    if not isinstance(target, _ast.Attribute):
                        line_numbers.append(target.lineno)

        return tuple(line_numbers)

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
                    if expressions.value \
                            .__dict__.get('func') \
                            .__dict__.get('id') \
                            in self.MUTABLE_TYPES:
                        line_numbers.append(expressions.lineno)

        return line_numbers

    def set_encapsulated_attribs_line_numbers(self):

        line_numbers = []
        if not isinstance(self.definition, _ast.FunctionDef):
            return line_numbers

        if self.definition.name != '__init__':

            for expressions in self.definition.body:
                if isinstance(expressions, _ast.Assign):
                    for target in expressions.targets:
                        # check for keyword 'self'
                        try:
                            value = target.value.value.id
                            if value == 'self':
                                line_numbers.append(target.lineno)
                        except AttributeError:
                            continue
        return line_numbers

    def setter_or_getters_def_names_line_numbers(self):

        line_numbers = []
        if not isinstance(self.definition, _ast.FunctionDef):
            return line_numbers

        if self.definition.name.startswith('set') or self.definition.name.startswith('get'):
            line_numbers.append(self.definition.lineno)
        return line_numbers
