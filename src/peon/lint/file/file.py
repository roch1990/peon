import typing

from peon.lint.file.line import Line
from peon.lint.file.statements import Statements


class File:

    def __init__(
            self,
            name: str,
            body: typing.Tuple[str],
    ):
        self.name = name
        self.body = body
        self.return_statement: typing.Tuple[Line] = Statements(text=self.body, statement=Statements.RETURN_STATEMENT).check()  # peon: exclude
        self.func_statement: typing.Tuple[Line] = Statements(text=self.body, statement=Statements.FUNC_STATEMENT).check()  # peon: exclude
        self.class_statement: typing.Tuple[Line] = Statements(text=self.body, statement=Statements.CLASS_STATEMENT).check()  # peon: exclude
        self.lines: typing.Tuple[Line] = Statements(text=self.body, statement=Statements.ALL_LINES).check()  # peon: exclude
