"""
test_example_079_using_pytest_parametrize.py

This test demonstrates how to use pytest.mark.parametrize to
run a test with different input values.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.mark.parametrize(
    "input_value,expected_length",
    [
        ("hello", 5),
        ("pytest", 6),
        ("chatgpt", 7),
    ]
)
def test_string_length(input_value, expected_length):
    assert len(input_value) == expected_length
