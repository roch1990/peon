from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple
from peon.src.lint.links.links import PrincipleLink


class NoStatementsInTestMethodsExceptAssert(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No statements in test methods except assert'
        self.link = PrincipleLink.NO_STATEMENTS_AT_TEST_METHODS_EXCEPT_ASSERT

    def lint_functions(self, functions: tuple):
        line_numbers = []
        for func in functions:
            check_result: tuple = func.non_assert_methods_at_test_function()

            if not check_result:
                continue

            line_numbers += check_result
        return line_numbers
