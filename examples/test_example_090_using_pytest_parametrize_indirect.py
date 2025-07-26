"""
test_example_090_using_pytest_parametrize_indirect.py

This test demonstrates indirect parametrization where parameters
are passed to fixtures instead of directly to tests.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture
def data(request):
    return request.param * 2

@pytest.mark.parametrize("data", [1, 2, 3], indirect=True)
def test_indirect_param(data):
    assert data in [2, 4, 6]
