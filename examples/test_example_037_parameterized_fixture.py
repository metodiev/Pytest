"""
test_example_037_parameterized_fixture.py

This test module demonstrates parameterized fixtures in pytest.

Tests:
- Run a test multiple times with different fixture values.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_is_positive(number):
    assert number > 0
