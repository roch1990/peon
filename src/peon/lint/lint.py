from typing import List

from peon.lint.file.analyze import InternalFileStruct
from peon.lint.file.file import File
from peon.lint.file.function_def.function import Function
from peon.lint.principles.principles import Principle


class Lint:

    def __init__(
            self,
            files: tuple,
    ):
        self.files = files

    def project(self):

        for file in self.files:

            print(f'check {file}')

            file = File(file)
            analyze = InternalFileStruct(file)
            analyze.check()

            # check for plain functions
            if not analyze.func_definitions and not analyze.class_definitions:
                continue

            # check plain functions
            self.lint_function_list(
                function_list=analyze.func_definitions,
                file=file,
            )

            # check classes
            for cls in analyze.class_definitions:

                methods = cls.converted_methods()
                self.lint_function_list(
                    function_list=methods,
                    file=file,
                )

    def lint_function_list(self, function_list: List[Function], file: File):

        for func in function_list:
            principles = Principle(
                file_object=file,
                output_channel='stdout',
                returned_expression=func.returned_value(),
                static_decorator=func.static_or_private(),
            )
            principles.no_null(func.returned_value().line_number)
            principles.no_static_methods_and_not_even_private_ones(func.definition.lineno)
