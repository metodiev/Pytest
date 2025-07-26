"""
test_example_035_test_ordering.py

This test module demonstrates controlling test execution order.

Notes:
- pytest runs tests in file system order by default.
- For precise control, use `pytest-order` plugin:
    pip install pytest-order

Tests:
- Mark tests to run first, last, or in a specific sequence.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.mark.order(2)
def test_second():
    print("Running second")
    assert True

@pytest.mark.order(1)
def test_first():
    print("Running first")
    assert True

@pytest.mark.order(-1)
def test_last():
    print("Running last")
    assert True
