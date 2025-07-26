"""
test_example_026_parametrize_with_ids.py

This test module demonstrates using pytest's parametrize decorator
with custom IDs for clearer test output.

Tests:
- Check if numbers are even or odd with descriptive test IDs.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "odd"),
        (2, "even"),
        (3, "odd"),
        (4, "even"),
    ],
    ids=["one", "two", "three", "four"]
)
def test_even_odd(number, expected):
    result = "even" if number % 2 == 0 else "odd"
    assert result == expected
