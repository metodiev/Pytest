"""
test_example_051_custom_marker_usage.py

This test module demonstrates defining and using custom pytest markers.

Usage:
- Register markers in pytest.ini before using
- Run tests with markers selectively

Example pytest.ini entry:

[pytest]
markers =
    integration: mark tests as integration tests
    slow: mark tests as slow-running

Usage:
- Run all tests: pytest -v
- Run only integration tests: pytest -v -m integration
"""

import pytest

@pytest.mark.integration
def test_integration_case():
    assert 1 + 1 == 2

@pytest.mark.slow
def test_slow_case():
    import time
    time.sleep(1)
    assert True
