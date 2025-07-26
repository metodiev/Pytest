"""
test_example_085_using_pytest_tmp_path.py

This test demonstrates using the tmp_path fixture to create
temporary files and directories safely.

Usage:
- Run: `pytest -v`
"""

def test_create_temp_file(tmp_path):
    temp_file = tmp_path / "testfile.txt"
    temp_file.write_text("Hello, pytest!")

    content = temp_file.read_text()
    assert content == "Hello, pytest!"
