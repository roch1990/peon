
class Report:

    NOTHING = ''

    def __init__(self, text: str):
        self.text = text

    def to_stdout(self):
        print(self.text)

    def to_file(self):
        pass
