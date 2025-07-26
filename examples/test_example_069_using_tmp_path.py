"""
test_example_069_using_tmp_path.py

This test demonstrates usage of pytest's tmp_path fixture to create
temporary directories and files that are cleaned up after the test.

Usage:
- Run: `pytest -v`
"""

def test_create_file_in_tmp_path(tmp_path):
    # Create a temporary file path
    file = tmp_path / "test_file.txt"
    
    # Write content to the file
    file.write_text("Hello pytest!")
    
    # Read back and assert
    content = file.read_text()
    assert content == "Hello pytest!"
