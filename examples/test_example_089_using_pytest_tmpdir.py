"""
test_example_089_using_pytest_tmpdir.py

This test demonstrates using the tmpdir fixture to create temporary
directories and files during tests.

Usage:
- Run: `pytest -v`
"""

def test_create_file_in_tmpdir(tmpdir):
    temp_file = tmpdir.join("tempfile.txt")
    temp_file.write("Hello from tmpdir!")

    content = temp_file.read()
    assert content == "Hello from tmpdir!"
