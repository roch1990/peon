import sys

from peon.src.lint.principles.principles import Principle


class LintFileHierarchy:

    def __init__(self, classes: tuple, functions: tuple):
        self.classes = classes
        self.functions = functions


class Lint:

    def __init__(
            self,
            files: tuple,
            output_channel: str,
    ):
        self.files = files
        self.output_channel = output_channel

    def project(self):
        reports = []

        principles = Principle(
            files=self.files,
            output_channel=self.output_channel,
        )
        reports.append(principles.no_null())
        reports.append(principles.no_code_in_constructors())
        reports.append(principles.no_getters_and_setters())
        reports.append(principles.no_mutable_objects())
        reports.append(principles.no_readers_parsers_or_controllers_or_sorters_and_so_on())
        reports.append(principles.no_static_methods_and_not_even_private_ones())
        reports.append(principles.no_instanceof_or_type_casting_or_reflection())
        reports.append(principles.no_statements_in_test_methods_except_assert())
        reports.append(principles.no_inheritance())

        code_with_vulnerabilities = False
        if reports:
            for report in reports:
                report_done = report.send()
                code_with_vulnerabilities = code_with_vulnerabilities or report_done

        if code_with_vulnerabilities:
            sys.exit(1)
