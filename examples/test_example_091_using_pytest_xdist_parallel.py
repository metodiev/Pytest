"""
test_example_091_using_pytest_xdist_parallel.py

This test demonstrates running tests in parallel using pytest-xdist.

Usage:
- Install pytest-xdist: `pip install pytest-xdist`
- Run tests in parallel: `pytest -n 4 -v`
"""

import time

def test_sleep_1():
    time.sleep(1)
    assert True

def test_sleep_2():
    time.sleep(1)
    assert True

def test_sleep_3():
    time.sleep(1)
    assert True

def test_sleep_4():
    time.sleep(1)
    assert True
