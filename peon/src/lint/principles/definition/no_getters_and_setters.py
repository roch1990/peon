from typing import Tuple

from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple
from peon.src.lint.links.links import PrincipleLink
from peon.src.project.file.function_def.function import FunctionLint


class NoGettersAndSetters(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No getters and setters'
        self.link = PrincipleLink.NO_GETTERS_AND_SETTERS

    def lint_functions(self, functions: Tuple[FunctionLint]):

        line_numbers = []
        for func in functions:
            check_result: list = func.setter_or_getters_def_names_line_numbers() + \
                                 func.set_encapsulated_attribs_line_numbers()

            if not check_result:
                continue
            line_numbers += check_result

        return line_numbers
