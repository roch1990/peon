import pytest

from peon.src.lint.report.report import Report
from peon.src.lint.report.report_channels import ReportChannels


def test_constructor():
    assert Report(text='test', channel=ReportChannels.stdout).text == 'test'


def test_text_is_none():
    assert Report(text=None, channel=ReportChannels.stdout).to_stdout() is False


def test_text_is_empty():
    assert Report(text='', channel=ReportChannels.stdout).to_stdout() is False


def test_text_is_filled():
    assert Report(text='test message', channel=ReportChannels.stdout).to_stdout() is True


def test_text_has_wrong_type():
    assert Report(text=[], channel=ReportChannels.stdout).to_stdout() is False
