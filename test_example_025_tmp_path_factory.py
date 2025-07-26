"""
test_example_025_tmp_path_factory.py

This test module demonstrates how to use pytest's `tmp_path_factory` fixture
to create shared temporary directories between tests or fixtures.

Fixtures:
- tmp_path_factory: Creates named, reusable temp directories across tests

Tests:
- Write and read from a shared directory

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="session")
def shared_temp_dir(tmp_path_factory):
    # Create a shared directory under /tmp with a consistent name
    dir_path = tmp_path_factory.mktemp("shared-data")
    return dir_path

def test_write_shared_file(shared_temp_dir):
    file_path = shared_temp_dir / "example.txt"
    file_path.write_text("Hello from test 1")
    assert file_path.exists()

def test_read_shared_file(shared_temp_dir):
    file_path = shared_temp_dir / "example.txt"
    # This test depends on test_write_shared_file running first
    # In real cases, you'd probably populate the file in a fixture
    content = file_path.read_text() if file_path.exists() else ""
    assert "Hello" in content
