import _ast

from peon.project.file.function_def.expression.returned_expr import ReturnedExpression


def test_return_value_is_func():
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Attribute(
                    value=_ast.Name(id='Function', ctx=_ast.Load()), attr='staticm', ctx=_ast.Load(),
                ), args=[], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is True


def test_return_value_is_int_one():
    # when method return 1
    assert ReturnedExpression(_ast.Return(value=_ast.Num(n=1), lineno=1)).value_not_none() is True


def test_return_value_is_int_zero():
    # when method return 0
    assert ReturnedExpression(_ast.Return(value=_ast.Num(n=0), lineno=1)).value_not_none() is True


def test_return_value_is_float_zero():
    # when method return 0.0
    assert ReturnedExpression(_ast.Return(value=_ast.Num(n=0.0), lineno=1)).value_not_none() is True


def test_return_value_is_float_limit_to_zero():
    # when method return 0.0000000000000000000000001
    assert ReturnedExpression(
        _ast.Return(value=_ast.Num(n=0.0000000000000000000000001), lineno=1),
    ).value_not_none() is True


def test_return_value_is_empty_string():
    # when method return ''
    assert ReturnedExpression(_ast.Return(value=_ast.Str(s=''), lineno=1)).value_not_none() is False


def test_return_value_is_filled_string():
    # when method return 'test'
    assert ReturnedExpression(_ast.Return(value=_ast.Str(s='test'), lineno=1)).value_not_none() is True


def test_return_value_is_empty_joined_string():
    # when method return ''
    assert ReturnedExpression(_ast.Return(value=_ast.JoinedStr(values=[]), lineno=1)).value_not_none() is False


def test_return_value_is_filled_joined_string():
    # when method return '{}{}{}'.format('a', 'b', 'c')
    assert ReturnedExpression(_ast.Return(value=_ast.JoinedStr(values=['a', 'b', 'c']), lineno=1)).value_not_none() is True


def test_return_value_is_none():
    # when method return None
    assert ReturnedExpression(_ast.Return(value=_ast.NameConstant(value=None), lineno=1)).value_not_none() is False


def test_return_value_is_class_constant():
    # when method return SomeClass.CONSTANT
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Attribute(value=_ast.Name(id='SomeClass', ctx=_ast.Load()), attr='CONSTANT', ctx=_ast.Load()),
            lineno=1,
        ),
    ).value_not_none() is True


def test_return_value_is_empty_list():
    # when method return []
    assert ReturnedExpression(
        _ast.Return(value=_ast.List(elts=[], ctx=_ast.Load()), lineno=1),
    ).value_not_none() is False


def test_return_value_is_filled_list():
    # when method return ['1']
    assert ReturnedExpression(
        _ast.Return(value=_ast.List(elts=['1'], ctx=_ast.Load()), lineno=1),
    ).value_not_none() is True


def test_return_value_is_empty_tuple():
    # when method return ()
    assert ReturnedExpression(
        _ast.Return(value=_ast.Tuple(elts=[], ctx=_ast.Load()), lineno=1),
    ).value_not_none() is False


def test_return_value_is_filled_tuple():
    # when method return ('1')
    assert ReturnedExpression(
        _ast.Return(value=_ast.Tuple(elts=['1'], ctx=_ast.Load()), lineno=1),
    ).value_not_none() is True


def test_return_value_is_empty_dict():
    # when method return {}
    assert ReturnedExpression(
        _ast.Return(value=_ast.Dict(keys=[], values=[]), lineno=1),
    ).value_not_none() is False


def test_return_value_is_filled_dict():
    # when method return {'1': '2'}
    assert ReturnedExpression(
        _ast.Return(value=_ast.Dict(keys=['1'], values=['2']), lineno=1),
    ).value_not_none() is True


def test_return_value_is_empty_dict_by_keyword():
    # when method return dict()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='dict', ctx=_ast.Load()), args=[], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is False


def test_return_value_is_filled_dict_by_keyword():
    # when method return dict(a='b')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='dict', ctx=_ast.Load()), args=[],
                keywords=[_ast.keyword(arg='a', value=_ast.Str(s='b'))],
            ),
            lineno=1,
        ),
    ).value_not_none() is True


def test_return_value_is_empty_list_by_keyword():
    # when method return list()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='list', ctx=_ast.Load()), args=[], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is False


def test_return_value_is_filled_list_by_keyword():
    # when method return list('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='list', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is True


def test_return_value_is_empty_set_by_keyword():
    # when method return set()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='set', ctx=_ast.Load()), args=[], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is False


def test_return_value_is_filled_set_by_keyword():
    # when method return set('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='set', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is True


def test_return_value_is_empty_tuple_by_keyword():
    # when method return tuple()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='tuple', ctx=_ast.Load()), args=[], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is False


def test_return_value_is_filled_tuple_by_keyword():
    # when method return tuple('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='tuple', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is True


def test_return_value_is_empty_frozenset_by_keyword():
    # when method return frozenset()
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='frozenset', ctx=_ast.Load()), args=[], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is False


def test_return_value_is_filled_frozenset_by_keyword():
    # when method return frozenset('1')
    assert ReturnedExpression(
        _ast.Return(
            value=_ast.Call(
                func=_ast.Name(id='frozenset', ctx=_ast.Load()), args=[_ast.Str(s='1')], keywords=[],
            ),
            lineno=1,
        ),
    ).value_not_none() is True


def test_return_is_empty():
    # when method return nothing, not None, only 'return'
    assert ReturnedExpression(
        _ast.Return(
            value=None,
            lineno=1,
        ),
    ).value_not_none() is False
