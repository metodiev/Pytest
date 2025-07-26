"""
test_example_064_class_scope_fixture.py

This test demonstrates using a class-scoped fixture, which runs
once per test class, before the first test method and after the
last one.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="class")
def setup_class_resource():
    print("\n[Setup - Class] Initializing resource for class")
    resource = {"initialized": True}
    yield resource
    print("[Teardown - Class] Cleaning up resource for class")

class TestClassScope:

    def test_method_1(self, setup_class_resource):
        assert setup_class_resource["initialized"]

    def test_method_2(self, setup_class_resource):
        assert "initialized" in setup_class_resource
