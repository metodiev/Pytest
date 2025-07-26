"""
test_example_030_parametrize_indirect_fixtures.py

This test module demonstrates indirect parametrization with pytest fixtures.

Concept:
- Using `indirect=True` in `@pytest.mark.parametrize` allows parameters
  to be passed to fixtures, not just test functions.

Tests:
- Setup data differently based on parameter values using fixtures.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture
def data(request):
    param = request.param
    return f"data_for_{param}"

@pytest.mark.parametrize("data", ["alpha", "beta", "gamma"], indirect=True)
def test_indirect_param(data):
    assert data.startswith("data_for_")
