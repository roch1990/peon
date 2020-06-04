from src.lint.links.links import PrincipleLink


def test_no_null():
    assert PrincipleLink.NO_NULL == 'https://www.yegor256.com/2014/05/13/why-null-is-bad.html'


def test_no_code_in_constructors():
    assert PrincipleLink.NO_CODE_IN_CONSTRUCTORS == 'https://www.yegor256.com/2015/05/07/ctors-must-be-code-free.html'


def test_no_getters_and_setters():
    assert PrincipleLink.NO_GETTERS_AND_SETTERS == 'https://www.yegor256.com/2014/09/16/getters-and-setters-are-evil.html'


def test_no_mutable_objects():
    assert PrincipleLink.NO_MUTABLE_OBJECTS == 'https://www.yegor256.com/2014/06/09/objects-should-be-immutable.html'


def test_no_static_method():
    assert PrincipleLink.NO_STATIC_METHODS == 'https://www.yegor256.com/2017/02/07/private-method-is-new-class.html'


def test_no_reflection():
    assert PrincipleLink.NO_REFLECTION == 'https://www.yegor256.com/2015/04/02/class-casting-is-anti-pattern.html'


def test_no_private_methods():
    assert PrincipleLink.NO_PRIVATE_METHODS == 'https://www.yegor256.com/2017/02/07/private-method-is-new-class.html'


def test_no_inheritance():
    assert PrincipleLink.NO_INHERITANCE == 'https://www.yegor256.com/2017/01/31/decorating-envelopes.html'


def test_no_endings():
    assert PrincipleLink.NO_ENDINGS == 'https://www.yegor256.com/2015/03/09/objects-end-with-er.html'


def test_no_statements_at_test_methods_except_assert():
    assert PrincipleLink.NO_STATEMENTS_AT_TEST_METHODS_EXCEPT_ASSERT == 'https://www.yegor256.com/2017/05/17/single-statement-unit-tests.html'
