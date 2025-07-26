"""
test_example_068_skip_and_xfail.py

This test demonstrates using pytest.mark.skip and pytest.mark.xfail
to control test skipping and expected failures.

Usage:
- Run: `pytest -v`
"""

import pytest
import sys

@pytest.mark.skip(reason="Skipping this test temporarily")
def test_skip_example():
    assert False  # This test will be skipped

@pytest.mark.xfail(sys.platform == "win32", reason="Fails on Windows")
def test_expected_failure():
    assert 1 == 2  # Known failing test on Windows
