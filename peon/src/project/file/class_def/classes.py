import _ast
from typing import Optional, Tuple

from peon.src.project.file.function_def.function import Function


class Class:
    """
    Class for handling in-code inspected class definitions
    """
    EMPTY_RETURNED_VALUE = None  # default constant for methods, that return nothing

    def __init__(
            self,
            definition: _ast.ClassDef,
    ):
        self.definition = definition
        self.name = definition.name
        self.functions = self.definition.body
        self.base_classes = definition.bases

    def constructor(self) -> Optional[Function]:
        """
        Check func definition for 'constructor' by name
        :return: bool
        """
        # iterate over all definitions from ast node body
        for func in self.functions:
            # check, that the aren't constants or assignment
            if isinstance(func, _ast.FunctionDef):
                # TODO: change None value to some other
                # return  that function if it's constructor else None
                return Function(func) if func.name == '__init__' else None
        return None

    def method_names(self) -> Tuple[str]:
        """
        Return all class defined methods
        :return: tuple with methods names
        """
        names = []
        # iterate over all definitions from ast node body
        for func in self.functions:
            # check, that the aren't constants or assignment
            if isinstance(func, _ast.FunctionDef):
                # append function name to list
                method_name: str = func.name
                names.append(method_name)
        # dont forget to convert list to immutable object
        return tuple(names)

    def converted_methods(self) -> Tuple[Function]:
        """
        Return all class methods as Function objects
        :return: tuple of class methods
        """
        converted_methods = []
        # iterate over all definitions from ast node body
        for func in self.functions:
            # check, that the aren't constants or assignment
            if isinstance(func, _ast.FunctionDef):
                # convert function from ast function object to local Function object
                converted_methods.append(Function(func))
        # dont forget to convert list to immutable object
        return tuple(converted_methods)

    def inherited(self) -> bool:
        """
        Check class for inheritance
        :return: bool
        """
        # check field existence
        if not self.base_classes:
            return False

        # check, that class is not inherit from any base class
        if len(self.base_classes) > 0:
            return True
        return False
