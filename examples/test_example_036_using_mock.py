"""
test_example_036_using_mock.py

This test module demonstrates how to use unittest.mock with pytest
to replace dependencies and control behavior during tests.

Tests:
- Mock a function call
- Assert the mock was called with expected arguments

Usage:
- Run: `pytest -v`
"""

from unittest.mock import patch

def fetch_data():
    # Imagine this calls an external API
    return "real data"

def process_data():
    data = fetch_data()
    return data.upper()

def test_process_data_with_mock():
    with patch("test_example_036_using_mock.fetch_data", return_value="mocked data") as mock_fetch:
    #with patch("__main__.fetch_data", return_value="mocked data") as mock_fetch:
        result = process_data()
        mock_fetch.assert_called_once()
        assert result == "MOCKED DATA"
