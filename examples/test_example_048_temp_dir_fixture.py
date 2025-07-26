"""
test_example_048_temp_dir_fixture.py

This test module demonstrates using pytest's tmp_path fixture for temporary directories.

Usage:
- Run: `pytest -v`
"""

def test_create_file_in_tmp(tmp_path):
    file = tmp_path / "test_file.txt"
    content = "Hello, pytest!"
    
    file.write_text(content)
    
    assert file.read_text() == content
    assert file.exists()
