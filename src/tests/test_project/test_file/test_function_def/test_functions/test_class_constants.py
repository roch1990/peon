from peon.project.file.function_def.function import Function


def test_empty_returned_value():
    assert Function.EMPTY_RETURNED_VALUE is True


def test_python_reflection_expressions():
    assert Function.PYTHON_REFLECTION_EXPRESSIONS == ('type', 'isinstance')


def test_mutable_types():
    assert Function.MUTABLE_TYPES == ('set', 'dict', 'list')
