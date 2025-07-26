"""
test_example_056_using_indirect_parametrize.py

This test module demonstrates the use of indirect parametrization in pytest.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture
def user(request):
    name = request.param
    return {"username": name, "active": True}

@pytest.mark.parametrize("user", ["alice", "bob", "charlie"], indirect=True)
def test_user_is_active(user):
    assert user["active"]
    assert user["username"] in ["alice", "bob", "charlie"]
