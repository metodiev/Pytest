"""
test_example_078_using_pytest_timeout.py

This test demonstrates usage of the pytest-timeout plugin to
fail tests that run longer than a given timeout.

Usage:
- Install pytest-timeout: `pip install pytest-timeout`
- Run: `pytest -v`
"""

import time
import pytest

@pytest.mark.timeout(2)  # Fail if test runs longer than 2 seconds
def test_fast_operation():
    time.sleep(1)  # Should pass
    assert True

@pytest.mark.timeout(2)
def test_slow_operation():
    time.sleep(3)  # Should fail due to timeout
    assert True
