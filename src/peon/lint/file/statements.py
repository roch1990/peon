import re
import typing

from peon.lint.file.line import Line


class Statements:

    CLASS_STATEMENT = 'class'
    FUNC_STATEMENT = 'def'
    RETURN_STATEMENT = 'return'
    ALL_LINES = None

    def __init__(self, text: typing.Tuple[str], statement: typing.Optional[str]):
        self.text = text
        self.statement = statement

    def check(self) -> typing.Tuple[Line]:
        statements = []
        line_number = 1

        for line in self.text:

            # TODO: pragma
            if '#' in line:
                if 'peon:' in line and 'exclude' in line:
                    continue

            splitted_line = tuple(re.findall(r"[\w\[\].,{}:']+", line))
            if not splitted_line:
                line_number += 1
                continue
            if self.statement in splitted_line or self.statement is None:
                statements.append(Line(words=splitted_line, line_number=line_number, raw_line=line))

            line_number += 1

        return tuple(statements)
