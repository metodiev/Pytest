"""
test_example_065_parametrized_fixture.py

This test demonstrates using a parametrized fixture to run tests
with different sets of data automatically.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_is_positive(number):
    assert number > 0
