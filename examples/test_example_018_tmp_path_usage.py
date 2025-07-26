"""
test_example_018_tmp_path_usage.py

This test module demonstrates how to use pytest's built-in 'tmp_path' fixture
to safely create and interact with temporary files and directories during testing.

Fixtures:
- tmp_path: Provides a unique temporary directory per test.

Tests:
- Write content to a file
- Read and verify that content

Usage:
- Run: `pytest`
"""

def test_create_temp_file(tmp_path):
    # tmp_path is a pathlib.Path object to a temporary directory
    file_path = tmp_path / "sample.txt"

    # Write to the file
    file_path.write_text("Hello, pytest!")

    # Read from the file
    content = file_path.read_text()

    # Verify the contents
    assert content == "Hello, pytest!"

def test_create_temp_subdir(tmp_path):
    # Create a subdirectory in the temp path
    sub_dir = tmp_path / "data"
    sub_dir.mkdir()

    # Create a file inside it
    file_path = sub_dir / "numbers.txt"
    file_path.write_text("1\n2\n3")

    # Read and verify
    lines = file_path.read_text().splitlines()
    assert lines == ["1", "2", "3"]
