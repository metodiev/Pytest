"""
test_example_062_module_scope_fixture.py

This test demonstrates using a module-scoped fixture, which runs
once per test module (file), no matter how many tests use it.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="module")
def mock_database():
    print("\n[Setup - Module] Connecting to mock database...")
    db = {"connected": True}
    yield db
    print("[Teardown - Module] Disconnecting from mock database...")

def test_db_connection_1(mock_database):
    assert mock_database["connected"]

def test_db_connection_2(mock_database):
    assert "connected" in mock_database
