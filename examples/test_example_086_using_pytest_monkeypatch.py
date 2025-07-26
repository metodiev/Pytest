"""
test_example_086_using_pytest_monkeypatch.py

This test demonstrates using monkeypatch to temporarily
modify functions or environment variables during tests.

Usage:
- Run: `pytest -v`
"""

import os
#import test_monkeypatch_example  # import your module explicitly


# def get_env_variable():
#     return os.getenv("MY_ENV_VAR", "default")

# def test_get_env_variable(monkeypatch):
#     monkeypatch.setenv("MY_ENV_VAR", "patched_value")
#     assert get_env_variable() == "patched_value"

# def test_monkeypatch_function(monkeypatch):
#     def fake_func():
#         return "mocked!"

#     monkeypatch.setattr(__name__, "get_env_variable", fake_func)
#     assert get_env_variable() == "mocked!"\



def get_env_variable():
    return os.getenv("MY_ENV_VAR", "default")

def test_get_env_variable(monkeypatch):
    monkeypatch.setenv("MY_ENV_VAR", "patched_value")
    assert get_env_variable() == "patched_value"

def test_monkeypatch_function(monkeypatch):
    def fake_func():
        return "mocked!"

    # Patch the function in the imported module explicitly
    monkeypatch.setattr(test_monkeypatch_example, "get_env_variable", fake_func)
    assert test_monkeypatch_example.get_env_variable() == "mocked!"

