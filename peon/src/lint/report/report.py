import sys


class Report:

    NOTHING = ''

    def __init__(self, text: str):
        self.text = text

    def to_stdout(self):
        print(self.text, file=sys.stderr)

    def to_file(self):
        if not self.text:
            return
        with open('peon_result.txt', 'w') as result:
            result.write(self.text)
