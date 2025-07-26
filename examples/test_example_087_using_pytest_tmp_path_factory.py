"""
test_example_087_using_pytest_tmp_path_factory.py

This test demonstrates using tmp_path_factory to create temporary
directories that can be reused across multiple tests or modules.

Usage:
- Run: `pytest -v`
"""

def test_tmp_path_factory_example(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("my_temp_dir")
    temp_file = temp_dir / "file.txt"
    temp_file.write_text("Hello from tmp_path_factory!")

    content = temp_file.read_text()
    assert content == "Hello from tmp_path_factory!"
