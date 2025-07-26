"""
test_example_019_yield_fixtures.py

This test module demonstrates the use of 'yield' fixtures in pytest,
which allow you to define setup and teardown logic in one place.

Fixtures:
- database_connection: Simulates connecting to and disconnecting from a database.

Tests:
- Check that the simulated database is available during the test.

Usage:
- Run: `pytest`
"""

import pytest

@pytest.fixture
def database_connection():
    # Setup: simulate opening a DB connection
    db = {"connected": True}
    print("\n[setup] Connecting to database...")
    yield db
    # Teardown: simulate closing the DB connection
    print("[teardown] Disconnecting from database...")
    db["connected"] = False

def test_db_is_connected(database_connection):
    assert database_connection["connected"] is True

def test_db_returns_data(database_connection):
    # Simulate retrieving data
    fake_data = {"user": "admin"}
    assert "user" in fake_data
