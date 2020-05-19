import ast
from typing import Optional, List

import _ast

from peon.lint.file.function_def.function import Function


class Class:
    EMPTY_RETURNED_VALUE = None

    def __init__(
            self,
            definition: _ast.ClassDef,
    ):
        self.definition = definition
        self.name = definition.name
        self.functions = self.definition.body

    def constructor(self) -> Optional[Function]:
        for func in self.functions:
            if isinstance(func, _ast.FunctionDef):
                return Function(func) if func.name == '__init__' else None
        return None

    def method_names(self) -> List[str]:
        names = []
        for func in self.functions:
            names.append(func.name)
        return names

    def converted_methods(self) -> List[Function]:
        converted_methods = []
        for func in self.functions:
            converted_methods.append(Function(func))
        return converted_methods
