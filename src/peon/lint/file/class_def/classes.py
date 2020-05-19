import _ast


class Class:
    EMPTY_RETURNED_VALUE = None

    def __init__(
            self,
            definition: _ast.ClassDef,
    ):
        self.definition = definition
