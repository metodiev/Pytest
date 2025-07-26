"""
test_example_017_expected_failures.py

This test module demonstrates how to use pytest's xfail marker to indicate
that certain tests are expected to fail (e.g., due to known bugs or unimplemented features).

Markers:
- @pytest.mark.xfail : Marks a test as expected to fail.

Usage:
- Run all tests: `pytest`
- See xfail results clearly with: `pytest -rxX`
"""

import pytest

@pytest.mark.xfail(reason="This feature is not implemented yet")
def test_feature_not_ready():
    # Simulate a test for a feature that's not implemented
    result = 1 + 1
    assert result == 3  # This will fail — and we expect it

@pytest.mark.xfail(reason="Known issue: negative division bug", strict=True)
def test_divide_by_negative():
    # Simulate a known bug when dividing by negative numbers
    result = 10 / -2
    assert result == -4  # Incorrect on purpose; expected to fail
