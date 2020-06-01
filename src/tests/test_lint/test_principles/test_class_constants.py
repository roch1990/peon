from peon.lint.principles.principles import Principle


def test_non_return_cases():
    assert Principle.NON_RETURN_CASES == ('None', '\'\'', '[]', '{}', '()')


def test_mutable_object_types():
    assert Principle.MUTABLE_OBJECT_TYPES == ('list', 'set', 'dict', '[', '{')


def test_restricted_endings():
    assert Principle.RESTRICTED_ENDINGS == ['er', 'es', 'ers', 'or']
