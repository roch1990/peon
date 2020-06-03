import pytest

from peon.src.lint.report.report import Report


def test_constructor():
    assert Report(text='test').text == 'test'


def test_text_is_none():
    assert Report(text=None).to_stdout() is None


def test_text_is_empty():
    assert Report(text='').to_stdout() is None


def test_text_is_filled():
    assert Report(text='test message').to_stdout() is None


def test_text_has_wrong_type():
    assert Report(text=[]).to_stdout() is None
