"""
test_example_073_using_tmp_path_factory.py

This test demonstrates using tmp_path_factory to create temporary
directories shared across tests or with custom structure.

Usage:
- Run: `pytest -v`
"""

def test_create_custom_tmp_dir(tmp_path_factory):
    # Create a temporary directory with a custom basename
    temp_dir = tmp_path_factory.mktemp("my_temp_dir")
    
    # Create a file inside that directory
    file = temp_dir / "sample.txt"
    file.write_text("Sample content")
    
    # Assert file was created with correct content
    assert file.read_text() == "Sample content"
