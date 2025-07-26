import pytest

def test_create_file_in_tmp_path(tmp_path):
    # Create a new file in the temporary directory
    file = tmp_path / "testfile.txt"
    file.write_text("Hello, pytest!")

    # Read the file content and verify
    content = file.read_text()
    assert content == "Hello, pytest!"

def test_tmp_path_is_empty_at_start(tmp_path):
    # The tmp_path directory should start empty for each test
    assert list(tmp_path.iterdir()) == []
