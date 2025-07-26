"""
test_example_075_using_autouse_fixtures.py

This test demonstrates the use of autouse fixtures that run
automatically for each test in the module.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup code
    print("\nSetup before test")
    yield
    # Teardown code
    print("\nTeardown after test")

def test_example_1():
    print("Executing test_example_1")
    assert True

def test_example_2():
    print("Executing test_example_2")
    assert True
