import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("\n[setup] Starting test")
    yield
    print("[teardown] Ending test")

def test_one():
    print("Running test_one")
    assert True

def test_two():
    print("Running test_two")
    assert 1 + 1 == 2
