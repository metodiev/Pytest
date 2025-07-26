"""
test_example_058_conftest_shared_fixtures.py

This test uses a fixture defined in conftest.py to demonstrate
how shared fixtures work in pytest.

Usage:
- Run: `pytest -v`

-----------------
conftest.py

Defines shared fixtures for use across multiple test files.
No need to import them — pytest finds them automatically.
----------------

import pytest

@pytest.fixture
def shared_data():
    return {"framework": "pytest", "language": "Python"}
"""

def test_shared_data_fixture(shared_data):
    assert shared_data["framework"] == "pytest"
    assert shared_data["language"] == "Python"