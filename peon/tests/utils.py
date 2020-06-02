import os

from peon.src.comandline.project_tree import ProjectTree


class TestProjectTree:

    def __init__(self):
        self.pythonpath = os.getenv('PYTHONPATH')
        self.project_tree = ProjectTree(
            path_to_project=[f'{self.pythonpath}/tests/fixtures'],
        )
