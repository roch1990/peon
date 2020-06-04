from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple
from peon.src.lint.links.links import PrincipleLink
from peon.src.project.file.class_def.classes import Class


class NoReadersParsersOrControllersOrSortersAndSoOn(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No readers, parsers or controllers or sorters and so on'
        self.link = PrincipleLink.NO_ENDINGS

    def lint_classes(self, cls: Class):
        line_numbers = []
        if cls.name.endswith('er') or \
                cls.name.endswith('or') or \
                cls.name.endswith('ers') or \
                cls.name.endswith('ors'):
            line_numbers.append(cls.definition.lineno)

        return line_numbers
