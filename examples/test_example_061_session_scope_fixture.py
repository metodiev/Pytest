"""
test_example_061_session_scope_fixture.py

This test demonstrates using a session-scoped fixture, which runs
once for the entire pytest session (not per test).

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture(scope="session")
def connect_to_service():
    print("\n[Setup - Session] Connecting to external service...")
    connection = {"status": "connected"}
    yield connection
    print("[Teardown - Session] Disconnecting from external service...")

def test_service_status_1(connect_to_service):
    assert connect_to_service["status"] == "connected"

def test_service_status_2(connect_to_service):
    assert "status" in connect_to_service
