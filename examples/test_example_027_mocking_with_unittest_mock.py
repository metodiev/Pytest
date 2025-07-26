"""
test_example_027_mocking_with_unittest_mock.py

This test module demonstrates using `unittest.mock` to mock functions and objects.

Tests:
- Mock a function call and verify behavior.

Usage:
- Run: `pytest -v`
"""

from unittest.mock import patch
import pytest

# Example module with a function to mock
class ExternalAPI:
    def get_data(self):
        # Imagine this calls an external service
        return {"status": "success", "data": 123}

def process_data():
    api = ExternalAPI()
    response = api.get_data()
    if response["status"] == "success":
        return response["data"]
    return None

def test_process_data_success():
    with patch.object(ExternalAPI, 'get_data', return_value={"status": "success", "data": 42}):
        result = process_data()
        assert result == 42

def test_process_data_failure():
    with patch.object(ExternalAPI, 'get_data', return_value={"status": "fail", "data": None}):
        result = process_data()
        assert result is None
