"""
test_example_050_using_xfail.py

This test module demonstrates pytest's xfail marker to mark tests
that are expected to fail.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.mark.xfail(reason="Known bug: function returns wrong output")
def test_known_failure():
    assert 1 + 1 == 3

@pytest.mark.xfail(strict=True, reason="Bug to be fixed soon")
def test_strict_xfail():
    # This test will fail the test suite if it unexpectedly passes
    assert 2 * 2 == 5

def test_normal():
    assert 2 + 2 == 4
