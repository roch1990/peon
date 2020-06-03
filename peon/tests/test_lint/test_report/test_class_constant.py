from peon.src.lint.report.report import Report


def test_class_constant():
    assert Report.NOTHING == ''
