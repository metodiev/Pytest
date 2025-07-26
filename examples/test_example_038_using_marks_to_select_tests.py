"""
test_example_038_using_marks_to_select_tests.py

This test module demonstrates using pytest marks to organize and select tests.

Tests:
- Mark tests with custom labels
- Run tests selectively using `-m` option

Usage:
- Run all tests: `pytest`
- Run only fast tests: `pytest -m fast`
- Run all except slow tests: `pytest -m "not slow"`
"""

import pytest

@pytest.mark.fast
def test_fast_1():
    assert 1 + 1 == 2

@pytest.mark.slow
def test_slow_1():
    import time
    time.sleep(1)
    assert True

@pytest.mark.fast
def test_fast_2():
    assert "a" * 3 == "aaa"
