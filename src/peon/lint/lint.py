from peon.lint.file.file import File
from peon.lint.principles.principles import Principle


class Lint:

    def __init__(
            self,
            files: tuple
    ):
        self.files = files

    def project(self):

        for file in self.files:
            with open(file, 'r') as py_file:
                file_body = tuple(py_file.readlines())
                file_object = File(body=file_body, name=file)
                principles = Principle(file_object=file_object, output_channel='stdout')
                principles.no_null()
                principles.no_mutable_objects()
                principles.no_code_in_constructors()
                principles.no_instanceof_or_type_casting_or_reflection()
                principles.no_static_methods_and_not_even_private_ones()
                principles.no_inheritance()
