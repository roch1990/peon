import _ast
from peon.project.file.function_def.function import Function

from peon.project.file.class_def.classes import Class


class ConstructorFixture:

    constructor_without_params = _ast.ClassDef(
        name='Test',
        body=[
            _ast.FunctionDef(
                name='__init__',
                body=[_ast.Pass()],
            ),
        ],
        bases=None,
    )
    empty_class = _ast.ClassDef(
        name='Test',
        body=[],
        bases=None,
    )
    class_without_constructor = _ast.ClassDef(
        name='Test',
        body=[
            _ast.FunctionDef(
                name='some_function',
                body=[_ast.Pass()],
            ),
        ],
        bases=None,
    )
    class_with_constructor_and_additional_method = _ast.ClassDef(
        name='Test',
        body=[
            _ast.FunctionDef(
                name='some_function',
                body=[_ast.Pass()],
            ),
            _ast.FunctionDef(
                name='__init__',
                body=[_ast.Pass()],
            ),
        ],
        bases=None,
    )
    class_with_inheritance = _ast.ClassDef(
        name='Test',
        body=[],
        bases=[_ast.ClassDef(name='TestParent')],
    )


def test_constructor_class_constructor_valid():
    assert isinstance(Class(ConstructorFixture.constructor_without_params).constructor(), Function)


def test_constructor_empty_class():
    assert Class(ConstructorFixture.empty_class).constructor() is None


def test_constructor_class_without_constructor():
    assert Class(ConstructorFixture.class_without_constructor).constructor() is None


def test_method_names_only_constructor():
    assert Class(ConstructorFixture.constructor_without_params).method_names() == ('__init__',)


def test_method_names_constructor_with_additional_method():
    assert Class(ConstructorFixture.class_with_constructor_and_additional_method).method_names() == ('some_function', '__init__')


def test_method_names_empty_class():
    assert Class(ConstructorFixture.empty_class).method_names() == ()


def test_converted_methods_constructor_with_additional_method():
    assert len(Class(ConstructorFixture.class_with_constructor_and_additional_method).converted_methods()) == 2
    assert isinstance(Class(ConstructorFixture.class_with_constructor_and_additional_method).converted_methods()[0], Function)
    assert isinstance(Class(ConstructorFixture.class_with_constructor_and_additional_method).converted_methods()[1], Function)


def test_converted_methods_empty_class():
    assert not len(Class(ConstructorFixture.empty_class).converted_methods())

def test_class_without_inheritance():
    assert Class(ConstructorFixture.empty_class).inherited() is False

def test_class_with_inheritance():
    assert Class(ConstructorFixture.class_with_inheritance).inherited() is True
