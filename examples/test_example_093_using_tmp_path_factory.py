import pytest

def test_multiple_tmp_dirs(tmp_path_factory):
    # Create two separate temporary directories
    temp_dir1 = tmp_path_factory.mktemp("data1")
    temp_dir2 = tmp_path_factory.mktemp("data2")

    # Create files in each temporary directory
    file1 = temp_dir1 / "file1.txt"
    file1.write_text("Content in data1")

    file2 = temp_dir2 / "file2.txt"
    file2.write_text("Content in data2")

    # Verify contents
    assert file1.read_text() == "Content in data1"
    assert file2.read_text() == "Content in data2"

    # Verify directories are distinct
    assert temp_dir1 != temp_dir2
