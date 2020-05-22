from typing import List

from peon.lint.file.analyze import InternalFileStruct
from peon.lint.file.file import File
from peon.lint.file.function_def.function import Function, FunctionParseResult
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

                principles = Principle(
                    file_object=file,
                    output_channel='stdout',
                    returned_expression=None,
                    static_decorator=False,
                    class_meta=cls,
                )
                principles.no_readers_parsers_or_controllers_or_sorters_and_so_on(cls.definition.lineno)
                principles.no_inheritance(cls.definition.lineno)

    def lint_function_list(self, function_list: List[Function], file: File):

        for func in function_list:
            principles = Principle(
                file_object=file,
                output_channel='stdout',
                returned_expression=func.returned_value(),
                static_decorator=func.static_or_private(),
                class_meta=None,
            )
            principles.no_null(func.returned_value().line_number)
            principles.no_static_methods_and_not_even_private_ones(func.definition.lineno)
            principles.no_instanceof_or_type_casting_or_reflection(func.reflection_at_line())
            principles.no_code_in_constructors(func.constructor_non_attribs_value_line_number())
            principles.no_statements_in_test_methods_except_assert(func.non_assert_methods_at_test_function())
