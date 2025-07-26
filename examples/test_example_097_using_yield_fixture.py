import pytest

@pytest.fixture
def resource():
    # Setup
    print("Setup resource")
    res = {"status": "open"}
    yield res
    # Teardown
    print("Teardown resource")
    res["status"] = "closed"

def test_resource_usage(resource):
    assert resource["status"] == "open"
