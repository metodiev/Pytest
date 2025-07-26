"""
test_example_044_fixture_finalizer.py

This test module demonstrates how to use fixture finalizers in pytest
to perform cleanup actions after tests.

Usage:
- Run: `pytest -v`
"""

import pytest

# @pytest.fixture
# def resource_with_cleanup():
#     print("\nSetup resource")
#     resource = {"name": "my_resource"}

#     def cleanup():
#         print("Cleanup resource")

#     # Register cleanup function to be called after the test
#     pytest.request.addfinalizer(cleanup)

#     return resource

# def test_using_resource(resource_with_cleanup):
#     assert resource_with_cleanup["name"] == "my_resource"


@pytest.fixture
def resource_with_cleanup(request):
    print("\nSetup resource")
    resource = {"name": "my_resource"}

    def cleanup():
        print("Cleanup resource")

    request.addfinalizer(cleanup)

    return resource

def test_using_resource(resource_with_cleanup):
    assert resource_with_cleanup["name"] == "my_resource"
