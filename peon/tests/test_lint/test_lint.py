import pytest
from peon.tests.utils import TestProjectTree

from peon.src.lint.lint import Lint
from peon.src.lint.report.report_channels import ReportChannels


def test_sucess():
    with pytest.raises(SystemExit):
        assert Lint(TestProjectTree().project_tree.inspect(), output_channel=ReportChannels.stdout).project() is None


def test_none_path():
    with pytest.raises(TypeError):
        assert Lint(None, output_channel=ReportChannels.stdout).project()


def test_empty_project():
    with pytest.raises(SystemExit):
        assert Lint([], output_channel=ReportChannels.stdout).project() is None
