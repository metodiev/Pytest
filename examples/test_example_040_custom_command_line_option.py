"""
test_example_040_custom_command_line_option.py

This test module demonstrates how to add and use custom command-line options in pytest.

Usage:
- Run with default: `pytest -v`
- Run with custom option: `pytest -v --env=staging`
"""

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

def test_environment(env):
    print(f"Running tests against environment: {env}")
    assert env in ["dev", "staging", "prod"]
