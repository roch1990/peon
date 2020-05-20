import re

from peon.lint.file.class_def.classes import Class
from peon.lint.file.file import File
from peon.lint.file.function_def.function import FunctionParseResult
from peon.lint.principles.links import PrincipleLink
from peon.lint.report.report import Report


class Principle:
    NON_RETURN_CASES = ('None', '\'\'', '[]', '{}', '()')
    MUTABLE_OBJECT_TYPES = ('list', 'set', 'dict', '[', '{')
    RESTRICTED_ENDINGS = ['er', 'es', 'ers', 'or']

    def __init__(
            self,
            file_object: File,
            output_channel: str,
            returned_expression: object,
            static_decorator: bool,
            class_meta: Class,
    ):
        self.file_object = file_object
        self.output_channel = output_channel
        self.returned_expression = returned_expression
        self.static_decorator = static_decorator
        self.class_meta = class_meta

    def no_null(self, line_number):
        check_result: FunctionParseResult = self.returned_expression

        if not check_result.return_not_none:
            Report(
                text=f'{self.file_object.path_to_file} [line:{line_number}]\n'
                f'commentary: No null rule {PrincipleLink.NO_NULL}\n',
            ).to_stdout()

    def no_code_in_constructors(self):
        pass

    def no_getters_and_setters(self):
        pass

    def no_mutable_objects(self):
        pass

    def no_readers_parsers_or_controllers_or_sorters_and_so_on(self, line_number):
        if self.class_meta.name.endswith('er') or \
                self.class_meta.name.endswith('or') or \
                self.class_meta.name.endswith('ers') or \
                self.class_meta.name.endswith('ors'):
            Report(
                text=f'{self.file_object.path_to_file} [line:{line_number}]\n'
                f"commentary: No 'er'/'ers' and etc endings {PrincipleLink.NO_ENDINGS}\n",
            ).to_stdout()

    def no_static_methods_and_not_even_private_ones(self, line_number):
        if self.static_decorator:
            Report(
                text=f'{self.file_object.path_to_file} [line:{line_number}]\n'
                f'commentary: No static methods or even private ones {PrincipleLink.NO_STATIC_METHODS}\n',
            ).to_stdout()

    def no_instanceof_or_type_casting_or_reflection(self, line_numbers):
        for line_number in line_numbers:
            Report(
                text=f'{self.file_object.path_to_file} [line:{line_number}]\n'
                f'commentary: No isinstance or reflection {PrincipleLink.NO_REFLECTION}\n',
            ).to_stdout()

    def no_public_methods_without_a_contract_interface(self):
        pass

    def no_statements_in_test_methods_except_assertThat(self):
        pass

    def no_orm(self):
        pass

    def no_inheritance(self, line_number):
        if self.class_meta.inherited():
            Report(
                text=f'{self.file_object.path_to_file} [line:{line_number}]\n'
                f'commentary: No inheritance {PrincipleLink.NO_INHERITANCE}\n',
            ).to_stdout()
