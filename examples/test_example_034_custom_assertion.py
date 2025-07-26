"""
test_example_034_custom_assertion.py

This test module demonstrates how to create custom assertion helper functions
to keep tests clean and reusable.

Tests:
- Use a custom assert helper to verify user data

Usage:
- Run: `pytest -v`
"""

def assert_user_valid(user):
    assert "id" in user and isinstance(user["id"], int), "User must have an integer 'id'"
    assert "name" in user and isinstance(user["name"], str) and user["name"], "User must have a non-empty 'name'"
    assert "email" in user and "@" in user["email"], "User must have a valid email"

def test_user_data():
    user = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }
    assert_user_valid(user)

def test_user_data_invalid():
    user = {
        "id": "one",
        "name": "",
        "email": "invalid-email"
    }
    try:
        assert_user_valid(user)
    except AssertionError as e:
        assert "User must have an integer 'id'" in str(e)
