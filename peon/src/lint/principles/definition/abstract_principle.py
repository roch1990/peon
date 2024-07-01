from peon.src.lint.report.report import Report
from peon.src.project.ast_analyze import InternalFileStruct
from peon.src.project.file.class_def.classes import Class
from peon.src.project.file.file import File


class AbstractPrinciple:

    def __init__(self, files: tuple, output_channel: str):
        self.principle_name = None
        self.files = files
        self.output_channel = output_channel
        self.link = None

    def check_rule(self) -> Report:

        problems_map = {}

        for file in self.files:

            file = File(file)
            file_hierarchy = InternalFileStruct(file)
            file_hierarchy.check()

            if not file_hierarchy.func_definitions and not file_hierarchy.class_definitions:
                continue

            classes = file_hierarchy.class_definitions
            functions = file_hierarchy.func_definitions

            function_lint_result = self.lint_functions(tuple(functions))
            class_methods_lint_result = []
            class_definition_lint_result = []
            for cls in classes:
                class_methods_lint_result += self.lint_functions(cls.converted_methods())
                class_definition_lint_result += self.lint_classes(cls)

            result_list = function_lint_result + class_methods_lint_result + class_definition_lint_result
            result_list.sort()

            if result_list:
                problems_map[file.path_to_file] = tuple(result_list)

        return self.report(problems_map)

    def lint_functions(self, functions: tuple):
        """
        Here magic happens
        :param functions:
        :return:
        """
        functions.__repr__()
        return []

    def lint_classes(self, classes: Class):
        classes.__repr__()
        return []

    def report(self, problem_map: dict):

        output = f'\nPrinciple: {self.principle_name}\n'
        for file, line_numbers in problem_map.items():
            for line_number in line_numbers:
                output += f'{file}:{line_number}\n'

        output += f'More information: {self.link}'

        if not problem_map:
            return Report(text='', channel=self.output_channel)

        return Report(
            text=output,
            channel=self.output_channel,
        )
