"""
test_example_052_using_tmp_path_factory.py

This test module demonstrates using pytest's tmp_path_factory fixture
to create multiple temporary directories.

Usage:
- Run: `pytest -v`
"""

def test_multiple_temp_dirs(tmp_path_factory):
    dir1 = tmp_path_factory.mktemp("data1")
    dir2 = tmp_path_factory.mktemp("data2")

    file1 = dir1 / "file1.txt"
    file2 = dir2 / "file2.txt"

    file1.write_text("Content for file1")
    file2.write_text("Content for file2")

    assert file1.read_text() == "Content for file1"
    assert file2.read_text() == "Content for file2"
