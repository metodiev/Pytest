"""
test_example_082_using_pytest_hook.py

This test demonstrates using a pytest hook to log test start events.

Usage:
- Run: `pytest -v`
"""

def pytest_runtest_setup(item):
    print(f"\nStarting test: {item.name}")

def test_sample_1():
    assert True

def test_sample_2():
    assert True
