import sys


class Report:

    NOTHING = ''

    def __init__(self, text: str):
        self.text = text

    def to_stdout(self):
        print(self.text, file=sys.stderr)
        exit(1)

    def to_file(self):
        pass
