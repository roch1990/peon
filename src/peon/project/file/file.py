class File:

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file

    def check_extension(self):
        file_extension_is_py = self.path_to_file.endswith('.py')
        return file_extension_is_py

    def open(self):
        try:
            file_object = open(self.path_to_file, 'r')
            return file_object.read()
        except (FileNotFoundError, IOError) as err:
            raise err
