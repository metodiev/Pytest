"""
test_example_022_parametrized_fixtures.py

This test module demonstrates how to use pytest's fixture parameterization
to run a test with multiple fixture values.

Fixtures:
- config_type: Yields different configuration types via parameters.

Tests:
- Check that the configuration contains the expected keys.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(params=["dev", "staging", "prod"])
def config_type(request):
    env = request.param
    configs = {
        "dev": {"debug": True, "db": "sqlite"},
        "staging": {"debug": False, "db": "postgres"},
        "prod": {"debug": False, "db": "mysql"},
    }
    return configs[env]

def test_config_has_required_keys(config_type):
    assert "debug" in config_type
    assert "db" in config_type
    assert isinstance(config_type["debug"], bool)
