import re

from peon.lint.file.file import File
from peon.lint.report.report import Report
from peon.lint.principles.links import PrincipleLink


class Principle:

    NON_RETURN_CASES = ('None', '\'\'', '[]', '{}', '()')
    MUTABLE_OBJECT_TYPES = ('list', 'set', 'dict', '[', '{',)
    RESTRICTED_ENDINGS = ['er', 'es', 'ers', 'or']

    def __init__(
            self,
            file_object: File,
            output_channel: str
    ):
        self.file_object = file_object
        self.output_channel = output_channel

    def no_null(self):
        for statement in self.file_object.return_statement:
            for word in statement.words:
                if word in Principle.NON_RETURN_CASES:
                    Report(text=f"{self.file_object.name} [line:{statement.line_number}]\n"
                    f"'{' '.join(statement.words)}'\n"
                    f"commentary: No null rule {PrincipleLink.NO_NULL}\n").to_stdout()

    def no_code_in_constructors(self):
        constructor = []

        for statement in self.file_object.lines:
            if not constructor and not 'def __init__' in statement.raw_line:
                continue
            if constructor and 'def' in statement.raw_line:
                break
            constructor.append(statement)

        constructor_body = []
        for statement in constructor:
            if not constructor_body and not '):' in statement.raw_line:
                continue
            if constructor_body and 'def' in statement.raw_line:
                break

            constructor_body.append(statement)

        object_props_assign_lines = []
        if constructor_body:
            constructor_body.pop(0)
        for line in constructor_body:
            if re.findall(r'^self', line.raw_line.lstrip(' ')) or '__init__' in line.raw_line:
                continue
            object_props_assign_lines.append(line)

        if object_props_assign_lines:
            for item in object_props_assign_lines:
                Report(text=f"{self.file_object.name} [line:{item.line_number}]\n"
                f"'{item.raw_line.lstrip(' ')[:-1]}'\n"
                f"commentary: No code in constructors {PrincipleLink.NO_CODE_IN_CONSTRUCTORS}\n").to_stdout()

    def no_getters_and_setters(self):
        pass

    def no_mutable_objects(self):
        constructor = []

        for statement in self.file_object.lines:
            if not constructor and not 'def __init__' in statement.raw_line:
                continue
            if constructor and 'def' in statement.raw_line:
                break
            constructor.append(statement)

        object_props_assign_lines = []
        for line in constructor:
            if 'self.' not in line.raw_line:
                continue
            object_props_assign_lines.append(line)

        for item in object_props_assign_lines:
            for mutable in Principle.MUTABLE_OBJECT_TYPES:
                if mutable in item.raw_line:
                    Report(text=f"{self.file_object.name} [line:{item.line_number}]\n"
                    f"'{item.raw_line.lstrip(' ')[:-1]}'\n"
                    f"commentary: No mutable objects {PrincipleLink.NO_MUTABLE_OBJECTS}\n").to_stdout()

    def no_readers_parsers_or_controllers_or_sorters_and_so_on(self):
        for statement in self.file_object.class_statement:
            for ending in Principle.RESTRICTED_ENDINGS:
                if ending in statement.raw_line:
                    Report(text=f"{self.file_object.name} [line:{statement.line_number}]\n"
                    f"'{statement.raw_line.lstrip(' ')[:-1]}'\n"
                    f"commentary: No 'er'/'ers' and etc endings {PrincipleLink.NO_ENDINGS}\n").to_stdout()

    def no_static_methods_and_not_even_private_ones(self):
        for statement in self.file_object.lines:
            if '@staticmethod(' in statement.raw_line:
                Report(text=f"{self.file_object.name} [line:{statement.line_number}]\n"
                f"'{statement.raw_line.lstrip(' ')[:-1]}'\n"
                f"commentary: No staticmethods {PrincipleLink.NO_PRIVATE_METHODS}\n").to_stdout()

            if 'def _' in statement.raw_line and not '__(' in statement.raw_line:
                Report(text=f"{self.file_object.name} [line:{statement.line_number}]\n"
                f"'{statement.raw_line.lstrip(' ')[:-1]}'\n"
                f"commentary: No private methods {PrincipleLink.NO_PRIVATE_METHODS}\n").to_stdout()

    def no_instanceof_or_type_casting_or_reflection(self):
        for statement in self.file_object.lines:
            if 'instanceof(' in statement.raw_line or 'type(' in statement.raw_line:
                Report(text=f"{self.file_object.name} [line:{statement.line_number}]\n"
                f"'{statement.raw_line.lstrip(' ')[:-1]}'\n"
                f"commentary: No reflection {PrincipleLink.NO_REFLECTION}\n").to_stdout()

    def no_public_methods_without_a_contract_interface(self):
        """
        I think this not for python
        :return:
        """
        pass

    def no_statements_in_test_methods_except_assertThat(self):
        pass

    def no_orm(self):
        pass

    def no_inheritance(self):
        for statement in self.file_object.class_statement:
            if '):' in statement.raw_line:
                Report(text=f"{self.file_object.name} [line:{statement.line_number}]\n"
                f"'{statement.raw_line.lstrip(' ')[:-1]}'\n"
                f"commentary: No inheritance {PrincipleLink.NO_INHERITANCE}\n").to_stdout()
