import pytest

@pytest.fixture
def managed_list():
    # Setup: create a list
    lst = []
    print("Setup: created list")
    yield lst
    # Teardown: clear the list
    lst.clear()
    print("Teardown: cleared list")

def test_append(managed_list):
    managed_list.append(1)
    assert managed_list == [1]

def test_empty_after_teardown(managed_list):
    # This test runs with a fresh list
    assert managed_list == []
