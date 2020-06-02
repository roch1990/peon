from peon.src.project.file.file import File


def test_path_to_file_is_none():
    assert File(None).check_extension() is False


def test_path_file_is_empty_string():
    assert File('').check_extension() is False


def test_path_file_without_extension():
    assert File('test_file').check_extension() is False


def test_path_file_with_wrong_extension():
    assert File('test_file.yp').check_extension() is False


def test_path_file_with_py_extension():
    assert File('test_file.py').check_extension() is True
