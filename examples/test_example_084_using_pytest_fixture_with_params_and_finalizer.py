"""
test_example_084_using_pytest_fixture_with_params_and_finalizer.py

This test demonstrates a parametrized fixture with a finalizer
to clean up after each test parameter.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=["alpha", "beta", "gamma"])
def setup_data(request):
    data = request.param
    print(f"\nSetup data: {data}")

    def cleanup():
        print(f"Cleanup data: {data}")

    request.addfinalizer(cleanup)
    return data

def test_using_setup_data(setup_data):
    print(f"Running test with: {setup_data}")
    assert isinstance(setup_data, str)
