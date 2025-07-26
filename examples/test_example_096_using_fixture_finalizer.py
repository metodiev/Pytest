import pytest

@pytest.fixture
def resource_with_finalizer(request):
    resource = {"opened": True}
    print("Setup: resource opened")

    def cleanup():
        resource["opened"] = False
        print("Teardown: resource closed")

    request.addfinalizer(cleanup)
    return resource

def test_resource(resource_with_finalizer):
    assert resource_with_finalizer["opened"] is True

