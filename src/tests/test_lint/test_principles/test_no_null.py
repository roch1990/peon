from peon.lint.principles.principles import Principle


def test_line_numbers_is_none():
    assert Principle(
        class_meta=None,
        file_object=None,
        output_channel=None,
        returned_expression=None,
        static_decorator=None,
    ).no_null(None) is None
