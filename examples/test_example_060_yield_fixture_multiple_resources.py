"""
test_example_060_yield_fixture_multiple_resources.py

This test demonstrates managing multiple setup/teardown operations
using a single yield-based fixture.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture
def multiple_resources():
    print("\n[Setup] Starting resource A")
    print("[Setup] Starting resource B")
    resources = {
        "res_a": "ResourceA",
        "res_b": "ResourceB"
    }

    yield resources

    print("[Teardown] Cleaning up resource B")
    print("[Teardown] Cleaning up resource A")

def test_using_multiple_resources(multiple_resources):
    assert multiple_resources["res_a"] == "ResourceA"
    assert multiple_resources["res_b"] == "ResourceB"
