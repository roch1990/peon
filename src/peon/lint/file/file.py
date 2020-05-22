class File:

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file

    def check_extension(self):
        if self.path_to_file[-3:] != '.py':
            return False
        return True

    def open(self):
        try:
            file_object = open(self.path_to_file, 'r')
            return file_object.read()
        except (FileNotFoundError, IOError) as err:
            raise err
