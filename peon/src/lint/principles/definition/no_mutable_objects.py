from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple
from peon.src.lint.links.links import PrincipleLink


class NoMutableObjects(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No mutable objects'
        self.link = PrincipleLink.NO_MUTABLE_OBJECTS

    def lint_functions(self, functions: tuple):
        line_numbers = []
        for func in functions:
            check_result: list = func.constructor_mutable_attribs_line_number()

            if not check_result:
                continue

            line_numbers += check_result

        return line_numbers
