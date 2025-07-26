"""
test_example_047_expected_exception.py

This test module shows how to check for expected exceptions in pytest.

Usage:
- Run: `pytest -v`
"""

import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_normal():
    assert divide(10, 2) == 5
