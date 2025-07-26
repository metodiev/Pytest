"""
test_example_067_parametrized_test_decorator.py

This test demonstrates using @pytest.mark.parametrize to
parametrize a test function with different inputs.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert input * input == expected
