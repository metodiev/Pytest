"""
test_example_053_clearing_cache.py

This test module demonstrates using pytest's cache fixture to
access and clear cached data during testing.

Usage:
- Run: `pytest -v`
"""

def test_cache_usage(cache):
    cache.set("my_key", "my_value")
    assert cache.get("my_key", None) == "my_value"

def test_cache_clearing(cache):
    cache.set("temp_key", "temp_value")
    assert cache.get("temp_key", None) == "temp_value"

    # Clear the cache entry by setting it to None (note: this doesn't remove the key entirely)
    cache.set("temp_key", None)
    assert cache.get("temp_key", "default") is None  # Returns None because we just set it
