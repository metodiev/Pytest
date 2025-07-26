"""
test_example_076_parametrized_fixtures.py

This test demonstrates using parametrized fixtures to run tests
with different data values.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=["apple", "banana", "cherry"])
def fruit(request):
    return request.param

def test_fruit_length(fruit):
    assert len(fruit) >= 5
