"""
test_example_043_using_parametrize.py

This test module demonstrates the use of @pytest.mark.parametrize
to run tests with multiple sets of inputs and expected outputs.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (2, 4),
        (3, 9),
        (4, 16),
        (5, 25)
    ]
)
def test_square(input_value, expected_output):
    assert input_value ** 2 == expected_output
