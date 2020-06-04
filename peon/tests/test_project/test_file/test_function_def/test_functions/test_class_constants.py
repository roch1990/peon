from peon.src.project.file.function_def.function import FunctionLint


def test_class_constant():
    assert FunctionLint.EMPTY_RETURNED_VALUE is True
    assert FunctionLint.PYTHON_REFLECTION_EXPRESSIONS == ('type', 'isinstance')
    assert FunctionLint.MUTABLE_TYPES == ('set', 'dict', 'list')
