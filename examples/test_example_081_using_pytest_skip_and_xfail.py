"""
test_example_081_using_pytest_skip_and_xfail.py

This test demonstrates how to skip tests dynamically and mark
tests expected to fail.

Usage:
- Run: `pytest -v`
"""

import pytest
import sys

def test_skip_example():
    if sys.platform == "win32":
        pytest.skip("Skipping this test on Windows")

    assert True  # Runs only if not Windows

@pytest.mark.xfail(reason="Known bug, fix pending")
def test_expected_failure():
    assert 1 == 2  # This test is expected to fail
