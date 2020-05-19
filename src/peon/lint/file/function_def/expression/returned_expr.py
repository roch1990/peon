import ast

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

        # if value is empty
        return bool(ReturnedExpression.EMPTY_VALUE)


if __name__ == '__main__':

    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Attribute(
                    value=_ast.Name(id='Function', ctx=_ast.Load()), attr='staticm', ctx=_ast.Load(),
                ), args=[], keywords=[],
            ),
        ),
    ).value_not_none() is True
    # return 1
    assert ReturnedExpression(_ast.Return(value=_ast.Num(n=1))).value_not_none() is True
    # return 0
    assert ReturnedExpression(_ast.Return(value=_ast.Num(n=0))).value_not_none() is True
    # return 0.0
    assert ReturnedExpression(_ast.Return(value=_ast.Num(n=0.0))).value_not_none() is True
    # return 0.0000000000000000000000001
    assert ReturnedExpression(_ast.Return(value=_ast.Num(n=0.0000000000000000000000001))).value_not_none() is True
    # return ''
    assert ReturnedExpression(_ast.Return(value=_ast.Str(s=''))).value_not_none() is False
    # return 'test'
    assert ReturnedExpression(_ast.Return(value=_ast.Str(s='test'))).value_not_none() is True
    # return None
    assert ReturnedExpression(_ast.Return(value=_ast.NameConstant(value=None))).value_not_none() is False
    # return SomeClass.CONSTANT
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Attribute(value=_ast.Name(id='SomeClass', ctx=_ast.Load()), attr='CONSTANT', ctx=_ast.Load()),
        ),
    ).value_not_none() is True
    # return []
    assert ReturnedExpression(_ast.Return(value=_ast.List(elts=[], ctx=_ast.Load()))).value_not_none() is False
    # return ['1']
    assert ReturnedExpression(_ast.Return(value=_ast.List(elts=['1'], ctx=_ast.Load()))).value_not_none() is True
    # return ()
    assert ReturnedExpression(_ast.Return(value=_ast.Tuple(elts=[], ctx=_ast.Load()))).value_not_none() is False
    # return ('1')
    assert ReturnedExpression(_ast.Return(value=_ast.Tuple(elts=['1'], ctx=_ast.Load()))).value_not_none() is True
    # return {}
    assert ReturnedExpression(_ast.Return(value=_ast.Dict(keys=[], values=[]))).value_not_none() is False
    # return {'1': '2'}
    assert ReturnedExpression(_ast.Return(value=_ast.Dict(keys=['1'], values=['2']))).value_not_none() is True
    # return dict()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='dict', ctx=_ast.Load()), args=[], keywords=[],
            ),
        ),
    ).value_not_none() is False
    # return dict(a='b')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='dict', ctx=_ast.Load()), args=[], keywords=[_ast.keyword(arg='a', value=_ast.Str(s='b'))],
            ),
        ),
    ).value_not_none()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='dict', ctx=_ast.Load()), args=[], keywords=[_ast.keyword(arg='a', value=_ast.Str(s='b'))],
            ),
        ),
    ).value_not_none() is True
    # return list()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='list', ctx=_ast.Load()), args=[], keywords=[],
            ),
        ),
    ).value_not_none() is False
    # return list('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='list', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
        ),
    ).value_not_none() is True
    # return set()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='set', ctx=_ast.Load()), args=[], keywords=[],
            ),
        ),
    ).value_not_none() is False
    # return set('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='set', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
        ),
    ).value_not_none() is True
    # return tuple()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='tuple', ctx=_ast.Load()), args=[], keywords=[],
            ),
        ),
    ).value_not_none() is False
    # return tuple('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='tuple', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
        ),
    ).value_not_none() is True
    # return frozenset()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='frozenset', ctx=_ast.Load()), args=[], keywords=[],
            ),
        ),
    ).value_not_none() is False
    # return frozenset('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='frozenset', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
        ),
    ).value_not_none() is True
