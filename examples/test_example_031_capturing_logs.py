"""
test_example_031_capturing_logs.py

This test module shows how to capture and test log output using pytest's `caplog` fixture.

Tests:
- Capture logs emitted during code execution
- Assert on log messages and levels

Usage:
- Run: `pytest -v`
"""

import logging
import pytest

logger = logging.getLogger(__name__)

def function_that_logs():
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")

def test_log_capture(caplog):
    with caplog.at_level(logging.INFO):
        function_that_logs()
    
    assert "Info message" in caplog.text
    assert "Warning message" in caplog.text
    assert "Error message" in caplog.text
    
    # Check log levels
    levels = [record.levelname for record in caplog.records]
    assert "INFO" in levels
    assert "WARNING" in levels
    assert "ERROR" in levels
