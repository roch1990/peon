import pytest
from peon.tests.utils import TestProjectTree

from peon.src.lint.lint import Lint
from peon.src.lint.report.report_channels import ReportChannels


def test_sucess():
    assert Lint(
        TestProjectTree().project_tree.inspect(),
        output_channel=ReportChannels.stdout,
        result_independence=True,
    ).project() is None


def test_none_path():
    with pytest.raises(TypeError):
        assert Lint(None, output_channel=ReportChannels.stdout, result_independence=True).project()


def test_empty_project():
    assert Lint([], output_channel=ReportChannels.stdout, result_independence=True).project() is None
