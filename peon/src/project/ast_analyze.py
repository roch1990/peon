import ast
from typing import List

from peon.src.project.file.class_def.classes import Class
from peon.src.project.file.file import File
from peon.src.project.file.function_def.function import Function


class InternalFileStruct(ast.NodeVisitor):

    def __init__(self, file: File):
        self.file = file
        self.class_definitions: List[Class] = []
        self.func_definitions: List[Function] = []

    def visit_FunctionDef(self, node):
        self.func_definitions.append(Function(node))

    def visit_ClassDef(self, node):
        self.class_definitions.append(Class(node))

    def check(self):
        tree = ast.parse(self.file.open())
        self.visit(tree)
