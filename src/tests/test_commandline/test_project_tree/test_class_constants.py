from peon.comandline.project_tree import ProjectTree


def test_default_exclude_folders():
    assert ProjectTree.DEFAULT_EXCLUDE_FOLDERS == ('build', 'venv')
