"""
test_example_080_using_pytest_fixture_params.py

This test demonstrates combining parametrized fixtures and
parametrize decorator for versatile test inputs.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

@pytest.mark.parametrize("multiplier", [10, 20])
def test_multiply(number, multiplier):
    result = number * multiplier
    assert result == number * multiplier
