"""
test_example_074_using_request_fixture.py

This test demonstrates using pytest's request fixture to access
contextual information about the currently running test.

Usage:
- Run: `pytest -v`
"""

import pytest

def test_request_fixture(request):
    # Access the name of the currently running test function
    current_test_name = request.node.name
    
    # Access the module where the test is located
    module_name = request.module.__name__
    
    assert current_test_name == "test_request_fixture"
    assert "test_example_074" in module_name
