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
