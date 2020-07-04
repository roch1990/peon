import argparse
import os
import sys

from peon.src.lint.report.report_channels import ReportChannels

from peon.src.comandline.project_tree import ProjectTree
from peon.src.lint.lint import Lint


class CommandLine:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Process some integers.')

    def argument_initialization(self):
        self.parser.add_argument(
            'path_to_project',
            metavar='PATH',
            type=str,
            nargs='*',
            help='path to your project or single file',
            default=os.path.curdir,
        )
        self.parser.add_argument(
            '--independence',
            action='store_true',
            help='this flag signify, that pre-commit hook is non blocking',
        )
        self.parser.add_argument(
            '-o',
            '--output',
            help='output to report file',
            action='store_const',
            default=ReportChannels.stdout,
            const=ReportChannels.file,
        )

    def parse_input(self):
        args = self.parser.parse_args()

        if args.path_to_project:

            project_tree = ProjectTree(args.path_to_project)
            files = project_tree.inspect()

            lint_result = Lint(
                files=tuple(files),
                output_channel=args.output,
                result_independence=args.independence,
            )
            lint_result.project()
