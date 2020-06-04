class File:

    PYTHON_FILE_EXTENSION = '.py'

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file

    def check_extension(self):
        """
        Check file extension. Need only '*.py' files.
        :return: bool
        """

        if not self.path_to_file:
            return False
        return self.path_to_file.endswith(self.PYTHON_FILE_EXTENSION)

    def open(self):
        try:
            file_object = open(self.path_to_file, 'r')
            return file_object.read()
        except (FileNotFoundError, IOError) as err:
            raise err

    def class_list(self, file: str, classes: tuple):
        for cls in classes:
            methods = cls.converted_methods()
            self.lint_function_list(
                functions=methods,
                file=file,
            )

    def function_list(self, file: str, functions: tuple):
        for func in function_list:
            principles.no_null(func.returned_value().line_number)
