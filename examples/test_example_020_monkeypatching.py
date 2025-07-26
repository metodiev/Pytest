"""
test_example_020_monkeypatching.py

This test module demonstrates how to use the 'monkeypatch' fixture
to temporarily override functions and environment variables during testing.

Fixtures:
- monkeypatch: Built-in pytest fixture for patching objects or environment safely.

Tests:
- Override a method in a module
- Patch an environment variable

Usage:
- Run: `pytest`

monkeypatch.setenv(key, value) – temporarily sets an environment variable
monkeypatch.setattr(obj, attr_name, new_value) – replaces a function or attribute
Everything is automatically restored after the test, so changes don’t leak.
"""

import os
import pytest

# A fake config module for testing
class config:
    @staticmethod
    def get_api_key():
        return os.getenv("API_KEY", "default-key")

def test_patch_environment_variable(monkeypatch):
    # Override the environment variable
    monkeypatch.setenv("API_KEY", "test-123")
    assert config.get_api_key() == "test-123"

def test_patch_function(monkeypatch):
    # Override the config.get_api_key function
    monkeypatch.setattr(config, "get_api_key", lambda: "mocked-key")
    assert config.get_api_key() == "mocked-key"
