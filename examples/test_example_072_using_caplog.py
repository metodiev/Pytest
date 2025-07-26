"""
test_example_072_using_caplog.py

This test demonstrates using pytest's caplog fixture to capture
logging output for assertions during tests.

Usage:
- Run: `pytest -v`
"""

import logging

logger = logging.getLogger(__name__)

def function_that_logs():
    logger.info("This is an info message")
    logger.error("This is an error message")

def test_logging_output(caplog):
    with caplog.at_level(logging.INFO):
        function_that_logs()

    assert "info message" in caplog.text
    assert "error message" in caplog.text
