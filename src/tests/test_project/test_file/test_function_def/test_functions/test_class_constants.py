from peon.project.file.function_def.function import Function


def test_class_constant():
    assert Function.EMPTY_RETURNED_VALUE is True
    assert Function.PYTHON_REFLECTION_EXPRESSIONS == ('type', 'isinstance')
    assert Function.MUTABLE_TYPES == ('set', 'dict', 'list')
