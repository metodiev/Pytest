"""
test_example_088_using_pytest_logging.py

This test demonstrates capturing and asserting log output using caplog.

Usage:
- Run: `pytest -v`
"""

import logging

def function_that_logs():
    logging.warning("This is a warning message")
    logging.error("This is an error message")

def test_logging_output(caplog):
    with caplog.at_level(logging.WARNING):
        function_that_logs()

    assert "warning message" in caplog.text
    assert "error message" in caplog.text
