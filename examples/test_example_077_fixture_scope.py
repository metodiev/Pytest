"""
test_example_077_fixture_scope.py

This test demonstrates fixture scopes: function, module, and session.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="function")
def func_scope_fixture():
    print("Setup function scope fixture")
    yield
    print("Teardown function scope fixture")

@pytest.fixture(scope="module")
def module_scope_fixture():
    print("Setup module scope fixture")
    yield
    print("Teardown module scope fixture")

@pytest.fixture(scope="session")
def session_scope_fixture():
    print("Setup session scope fixture")
    yield
    print("Teardown session scope fixture")

def test_one(func_scope_fixture, module_scope_fixture, session_scope_fixture):
    print("Executing test_one")
    assert True

def test_two(func_scope_fixture, module_scope_fixture, session_scope_fixture):
    print("Executing test_two")
    assert True
