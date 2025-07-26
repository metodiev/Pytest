"""
test_example_054_custom_command_line_option.py

This test module demonstrates adding a custom command-line option
to pytest and using it inside tests.

Usage:
- Run: `pytest -v --env=dev`
"""

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="Environment to run tests against"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

def test_environment(env):
    print(f"Running tests on environment: {env}")
    assert env in ("dev", "prod", "test")
