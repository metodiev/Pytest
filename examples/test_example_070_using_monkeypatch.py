"""
test_example_070_using_monkeypatch.py

This test demonstrates how to use the monkeypatch fixture to
temporarily modify functions, attributes, or environment variables.

Usage:
- Run: `pytest -v`
"""
import sys


def get_env_variable():
    import os
    return os.getenv("MY_VAR", "default")

def test_monkeypatch_env(monkeypatch):
    # Patch environment variable MY_VAR
    monkeypatch.setenv("MY_VAR", "patched_value")
    assert get_env_variable() == "patched_value"

def test_monkeypatch_function(monkeypatch):
    # Patch a function dynamically
    def fake_func():
        return "fake result"
    
    monkeypatch.setattr(sys.modules[__name__], "get_env_variable", fake_func)
    assert get_env_variable() == "fake result"
    # monkeypatch.setattr(__name__, "get_env_variable", fake_func)
    # assert get_env_variable() == "fake result"
