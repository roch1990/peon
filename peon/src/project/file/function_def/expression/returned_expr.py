import _ast


class ReturnedExpression:
    """
    class for processing "return" expression
    """

    EMPTY_VALUE = None
    RETURNED_ID = ['set', 'dict', 'list', 'frozenset', 'int', 'str', 'float', 'tuple']

    def __init__(self, expression: _ast.Return):
        self.definiton = expression
        self.line_number = expression.lineno

    def value_not_none(self) -> bool:
        """
        Return value of "return" expression
        :return:
        """
        item = self.definiton

        try:
            # mostly true way - return object
            if isinstance(item.value, _ast.Call) and isinstance(item.value.func, _ast.Attribute):
                return True

            # class constants etc
            elif isinstance(item.value, _ast.Attribute):
                return True

            # string object

            elif isinstance(item.value, _ast.Str):
                return bool(item.value.s)

            elif isinstance(item.value, _ast.JoinedStr):
                return bool(item.value.values)

            # None object and ... dunno what
            elif isinstance(item.value, _ast.NameConstant):
                return bool(item.value.value)

            # Numeric value
            elif isinstance(item.value, _ast.Num):
                # bool of 0 is False :)
                if int(item.value.n) == 0:
                    return True
                return bool(item.value.n)

            # list object
            elif isinstance(item.value, _ast.List):
                return bool(item.value.elts)

            # object like dict() or list()
            elif isinstance(item.value, _ast.Call):
                # check id of value (like 'dict' or 'list')
                if item.value.func.id in ReturnedExpression.RETURNED_ID:
                    # args and keywords - where object store values
                    return bool(item.value.args) or bool(item.value.keywords)

            # dict object
            elif isinstance(item.value, _ast.Dict):
                return bool(item.value.keys)

            # tuple object
            elif isinstance(item.value, _ast.Tuple):
                return bool(item.value.elts)
        except (AttributeError):
            # TODO: what can i do, when "_ast.Str not found into python3.8"?
            pass

        # if value is empty
        return bool(ReturnedExpression.EMPTY_VALUE)
