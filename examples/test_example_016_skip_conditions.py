"""
test_example_016_skip_conditions.py

This test module demonstrates how to skip tests conditionally using:
- pytest.skip() at runtime
- pytest.mark.skipif() for preconditions

Markers:
- @pytest.mark.smoke : Used to tag smoke tests.

Usage:
- Run all tests: `pytest`
- Run only smoke tests: `pytest -m smoke`
"""

import pytest
import sys

@pytest.mark.smoke
def test_skip_at_runtime():
    # Simulate skipping during test execution
    skip_reason = "Feature not implemented"
    pytest.skip(reason=skip_reason)
    assert True  # This line will not run

@pytest.mark.smoke
@pytest.mark.skipif(sys.platform != "linux", reason="Only runs on Linux")
def test_only_on_linux():
    # This test will be skipped on non-Linux systems
    assert True
