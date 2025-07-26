"""
test_example_046_custom_assertion_message.py

This test module shows how to provide custom assertion messages in pytest tests.

Usage:
- Run: `pytest -v`
"""

def test_custom_message():
    x = 5
    y = 10
    assert x >y, f"Expected x ({x}) to be greater than y ({y})"
