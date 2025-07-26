"""
test_example_083_using_pytest_fixture_finalizer.py

This test demonstrates using a fixture finalizer to perform cleanup
after a test runs.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture
def resource():
    print("\nSetup resource")
    yield
    print("\nCleanup resource")

def test_using_resource(resource):
    print("Test using resource")
    assert True
