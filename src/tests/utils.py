import os

from peon.comandline.project_tree import ProjectTree
from peon.lint.file.file import File


class TestProjectTree:

    def __init__(self):
        self.pythonpath = os.getenv('PYTHONPATH')
        self.project_tree = ProjectTree(
            path_to_project=f'{self.pythonpath}/tests/fixtures',
        )


class TestFile:

    def __init__(self):
        self.body = (
            'class Abstracter:',
            'def __init__(self, something: list):',
            'self.something = something',
            'return None',
        )
        self.file = File(name='test', body=self.body)
