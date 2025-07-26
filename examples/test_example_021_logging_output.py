"""
test_example_021_logging_output.py

This test module demonstrates how to capture and assert log output using the 'caplog' fixture.

Fixtures:
- caplog: Built-in pytest fixture to capture logging output during test execution.

Tests:
- Ensure expected log messages are emitted by a function.

Usage:
- Run: `pytest -v`
"""

import logging

# Simulated app logic that logs messages
def process_data():
    logging.info("Starting data processing...")
    logging.warning("Missing optional config, using defaults.")
    logging.info("Finished processing.")

def test_logging_messages(caplog):
    with caplog.at_level(logging.INFO):
        process_data()

    # Assert logs contain expected messages
    assert "Starting data processing..." in caplog.text
    assert "Missing optional config" in caplog.text
    assert "Finished processing." in caplog.text

    # Check specific log levels if needed
    warnings = [record for record in caplog.records if record.levelname == "WARNING"]
    assert len(warnings) == 1
    assert "Missing optional config" in warnings[0].message
