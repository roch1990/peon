from peon.src.lint.links.links import PrincipleLink
from peon.src.lint.principles.definition.abstract_principle import AbstractPrinciple
from peon.src.project.file.class_def.classes import Class


class NoInheritance(AbstractPrinciple):

    def __init__(self, files: tuple, output_channel: str):
        super().__init__(
            files=files,
            output_channel=output_channel,
        )
        self.principle_name = 'No inheritance'
        self.link = PrincipleLink.NO_INHERITANCE

    def lint_classes(self, cls: Class):
        line_numbers = []
        if cls.inherited():
            line_numbers.append(cls.definition.lineno)

        return line_numbers
