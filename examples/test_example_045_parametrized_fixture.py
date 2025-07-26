"""
test_example_045_parametrized_fixture.py

This test module shows how to create and use a parameterized fixture in pytest.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=["apple", "banana", "cherry"])
def fruit(request):
    return request.param

def test_fruit_length(fruit):
    assert len(fruit) > 0
