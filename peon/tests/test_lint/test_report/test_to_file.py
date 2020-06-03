import os

import pytest

from peon.src.lint.report.report import Report


class ReportToFileFixture:
    file_name = 'peon_result.txt'

    def clean(self):
        print(os.remove(self.file_name))

    def content(self):
        with open('peon_result.txt') as f:
            content = f.read()
        return content


def test_text_is_none():
    Report(text=None).to_file()
    with pytest.raises(FileNotFoundError):
        assert ReportToFileFixture().content()


def test_text_is_empty_string():
    Report(text='').to_file()
    with pytest.raises(FileNotFoundError):
        assert ReportToFileFixture().content()


def test_text_is_filled_string():
    Report(text='test').to_file()
    assert ReportToFileFixture().content() == 'test'
    ReportToFileFixture().clean()
