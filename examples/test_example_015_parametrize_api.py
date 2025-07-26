"""
test_example_015_parametrize_api.py

This test module demonstrates using pytest's @pytest.mark.parametrize decorator
to run the same test logic over multiple input values.

Marker used:
- @pytest.mark.api : Marks tests related to API calls.

Tests:
- test_api_endpoints: Simulates API endpoint GET requests with different URLs
  and checks for expected HTTP status codes.

Usage:
- Run all tests: `pytest`
- Run only API tests: `pytest -m api`

Make sure your pytest.ini includes the 'api' marker to avoid warnings.
"""

import pytest

@pytest.mark.api
@pytest.mark.parametrize("input_value, expected_status", [
    ("/users", 200),
    ("/posts", 200),
    ("/invalid", 404),
])
def test_api_endpoints(input_value, expected_status):
    # Simulate API response status based on the endpoint
    fake_api_responses = {
        "/users": 200,
        "/posts": 200,
        "/invalid": 404,
    }
    response_status = fake_api_responses.get(input_value, 500)
    assert response_status == expected_status
