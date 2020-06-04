from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple
from peon.src.lint.links.links import PrincipleLink
from peon.src.project.file.function_def.function import FunctionParseResult


class NoStaticMethodsAndNotEvenPrivateOnes(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No static methods and not even private ones'
        self.link = PrincipleLink.NO_STATIC_METHODS

    def lint_functions(self, functions: tuple):
        line_numbers = []
        for func in functions:
            if not func.static_or_private():
                continue

            check_result: FunctionParseResult = func.definition.lineno

            if not check_result:
                continue

            line_numbers.append(check_result)

        return line_numbers
