from peon.src.lint.links.links import PrincipleLink
from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple


class NoCodeInConstructor(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No code in constructor'
        self.link = PrincipleLink.NO_CODE_IN_CONSTRUCTORS

    def lint_functions(self, functions: tuple):
        line_numbers = []
        for func in functions:
            constructor_line_numbers: list = func.constructor_non_attribs_value_line_number()

            if not constructor_line_numbers:
                continue

            line_numbers += constructor_line_numbers

        return line_numbers
