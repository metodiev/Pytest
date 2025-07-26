"""
test_example_042_test_skipping.py

This test module demonstrates skipping tests with pytest.

Tests:
- Unconditionally skip a test
- Skip based on a condition
- Skip with a reason

Usage:
- Run: `pytest -v`
"""

import pytest
import sys

@pytest.mark.skip(reason="Skipping this test for demonstration")
def test_unconditional_skip():
    assert False  # This will not run

@pytest.mark.skipif(sys.platform == "win32", reason="Skip on Windows")
def test_skip_on_windows():
    assert True

def test_conditional_skip():
    if not hasattr(sys, "argv"):
        pytest.skip("Skipping because argv is not available")
    assert True
