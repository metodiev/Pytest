"""
test_example_039_fixture_scope.py

This test module demonstrates pytest fixture scopes.

Fixture scopes:
- function (default): setup/teardown per test function
- class: once per test class
- module: once per module
- session: once per test session

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="function")
def func_resource():
    print("\nSetup function resource")
    yield "func"
    print("Teardown function resource")

@pytest.fixture(scope="module")
def mod_resource():
    print("\nSetup module resource")
    yield "module"
    print("Teardown module resource")

def test_func_1(func_resource, mod_resource):
    assert func_resource == "func"
    assert mod_resource == "module"

def test_func_2(func_resource, mod_resource):
    assert func_resource == "func"
    assert mod_resource == "module"
