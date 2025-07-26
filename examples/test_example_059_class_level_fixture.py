"""
test_example_059_class_level_fixture.py

This test module shows how to use a fixture at the class level
using @pytest.mark.usefixtures.

Usage:
- Run: `pytest -v`
"""

import pytest

@pytest.fixture
def setup_environment():
    print("\n[Setup] Preparing environment for test")
    yield
    print("[Teardown] Cleaning up after test")

@pytest.mark.usefixtures("setup_environment")
class TestSampleSuite:

    def test_case_one(self):
        print(">> Running test_case_one")
        assert True

    def test_case_two(self):
        print(">> Running test_case_two")
        assert "py" in "pytest"
