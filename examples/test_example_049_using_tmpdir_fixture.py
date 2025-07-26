"""
test_example_049_using_tmpdir_fixture.py

This test module demonstrates using pytest's tmpdir fixture for temporary directories.

Usage:
- Run: `pytest -v`
"""

def test_write_and_read_tmpdir(tmpdir):
    file = tmpdir.join("sample.txt")
    content = "pytest tmpdir example"
    
    file.write(content)
    read_content = file.read()
    
    assert read_content == content
    assert file.check()
