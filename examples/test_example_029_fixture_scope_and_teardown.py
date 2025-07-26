"""
test_example_029_fixture_scope_and_teardown.py

This test module shows how to:
- Use different fixture scopes (function, module, session)
- Add teardown logic via `request.addfinalizer`

Tests:
- Demonstrate setup and teardown behavior with scoped fixtures

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="module")
def resource_setup(request):
    print("\n[Setup] Initializing resource")
    resource = {"status": "ready"}

    def teardown():
        print("\n[Teardown] Cleaning up resource")
        resource["status"] = "cleaned"

    request.addfinalizer(teardown)
    return resource

def test_resource_usage_one(resource_setup):
    assert resource_setup["status"] == "ready"

def test_resource_usage_two(resource_setup):
    assert resource_setup["status"] == "ready"
