"""
test_example_032_skip_and_xfail.py

This test module demonstrates usage of pytest's skip and xfail markers.

Tests:
- Skip tests conditionally or unconditionally
- Mark tests expected to fail (xfail)

Usage:
- Run: `pytest -v`

pytest marks:
Skip: Avoid running tests that don’t apply in certain environments or conditions.

Xfail(Expected Fail): Mark tests with known bugs or incomplete features without failing the build.

Makes test results clearer and easier to manage.
"""

import pytest
import sys

@pytest.mark.skip(reason="Demonstrating unconditional skip")
def test_skipped_unconditionally():
    assert False  # This will be skipped, so no failure.

@pytest.mark.skipif(sys.platform == "win32", reason="Fails on Windows")
def test_skipped_on_windows():
    assert True  # Skipped if running on Windows.

@pytest.mark.xfail(reason="Known bug #123")
def test_expected_to_fail():
    assert 1 == 2

@pytest.mark.xfail(run=False, reason="Feature not implemented yet")
def test_xfail_not_run():
    assert 1 == 1  # This test is marked xfail and will be skipped.
