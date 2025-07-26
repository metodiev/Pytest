"""
test_example_066_multiple_parametrized_fixtures.py

This test demonstrates combining multiple parametrized fixtures,
generating all possible parameter combinations.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=["apple", "banana"])
def fruit(request):
    return request.param

@pytest.fixture(params=[1, 2])
def number(request):
    return request.param

def test_fruit_number_combination(fruit, number):
    print(f"Testing combination: {fruit} and {number}")
    assert isinstance(fruit, str)
    assert isinstance(number, int)
