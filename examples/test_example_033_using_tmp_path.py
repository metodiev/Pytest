"""
test_example_033_using_tmp_path.py

This test module demonstrates using pytest's `tmp_path` fixture
to create temporary files and directories safely.

Tests:
- Create a temp file
- Write/read content
- Check file existence

Usage:
- Run: `pytest -v`
"""

def test_write_and_read(tmp_path):
    # Create a temporary file path
    file = tmp_path / "testfile.txt"

    # Write some text
    file.write_text("Hello, pytest!")

    # Read back the text
    content = file.read_text()
    assert content == "Hello, pytest!"

def test_create_directory(tmp_path):
    # Create a temporary directory
    subdir = tmp_path / "subdir"
    subdir.mkdir()

    # Create a file inside the directory
    file = subdir / "file.txt"
    file.write_text("data")

    # Verify file exists
    assert file.exists()
    assert file.read_text() == "data"
