"""
test_example_057_autouse_fixture.py

This test module demonstrates how to use autouse=True in a fixture,
which causes it to apply automatically to all tests in the module.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(autouse=True)
def print_before_and_after_each_test():
    print("\n[Setup] Before test runs")
    yield
    print("[Teardown] After test runs")

def test_one():
    print(">> Running test_one")
    assert 1 + 1 == 2

def test_two():
    print(">> Running test_two")
    assert "py" + "test" == "pytest"
