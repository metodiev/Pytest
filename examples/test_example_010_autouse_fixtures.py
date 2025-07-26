import pytest

@pytest.fixture(autouse=True)
def setup_teardown():
    print("\nSetup before test")
    yield
    print("Teardown after test")

def test_one():
    print("Running test_one")
    assert True

def test_two():
    print("Running test_two")
    assert True
