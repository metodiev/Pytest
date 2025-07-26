"""
test_example_023_custom_cli_options.py

This test module demonstrates how to define and use custom pytest command-line options.

Key Concepts:
- Add options with `pytest_addoption` in conftest.py
- Access values via `request.config.getoption()`

Tests:
- Behave differently depending on the value of a custom option: --env

Usage:
- Run with: `pytest --env=staging`

----------------
conftest.py
----------------
Registers a custom command-line option '--env' for pytest.


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev / staging / prod",
    )
"""

import pytest

@pytest.fixture
def environment(request):
    return request.config.getoption("--env")

def test_environment_variable(environment):
    assert environment in ["dev", "staging", "prod"]
