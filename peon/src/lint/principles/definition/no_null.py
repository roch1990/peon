from peon.src.lint.links.links import PrincipleLink
from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple
from peon.src.project.file.function_def.function import FunctionParseResult


class NoNull(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No null'
        self.link = PrincipleLink.NO_NULL

    def lint_functions(self, functions: tuple):
        line_numbers = []
        for func in functions:
            check_result: FunctionParseResult = func.returned_value()

            if not check_result:
                continue

            if not check_result.return_not_none:
                line_numbers.append(check_result.line_number)

        return line_numbers
