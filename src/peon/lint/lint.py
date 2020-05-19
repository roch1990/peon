from peon.lint.file.analyze import InternalFileStruct
from peon.lint.file.file import File
from peon.lint.file.function_def.function import Function
from peon.lint.principles.principles import Principle


class Lint:

    def __init__(
            self,
            files: tuple,
    ):
        self.files = files

    def project(self):

        for file in self.files:

            print(f'check {file}')

            file = File(file)
            analyze = InternalFileStruct(file)
            analyze.check()

            # check for plain functions
            if analyze.func_definitions is None:
                continue

            for func in analyze.func_definitions:

                returned = func.returned_value()
                principles = Principle(
                    file_object=file,
                    line_number='0',
                    check_result=returned,
                    output_channel='stdout',
                )
                principles.no_null()
