class Abstracter:

    def __init__(self, something: list):

        self.something = something
        if not self.something:
            self.something = []

    @staticmethod
    def abstract_function():
        return None

    def _privater(self):
        return None


class AbstractInheritor(Abstracter):

    def __init__(self, something):
        super().__init__(something=something)

        self.something_new = {}
        self. another_something_new = set()
