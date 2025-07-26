"""
test_example_063_function_scope_fixture.py

This test demonstrates the default 'function' scope of fixtures,
where the fixture setup and teardown happen before and after
each test function.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="function")
def temp_resource():
    print("\n[Setup - Function] Creating temporary resource")
    resource = {"status": "ready"}
    yield resource
    print("[Teardown - Function] Cleaning up temporary resource")

def test_temp_resource_1(temp_resource):
    assert temp_resource["status"] == "ready"

def test_temp_resource_2(temp_resource):
    assert "status" in temp_resource

