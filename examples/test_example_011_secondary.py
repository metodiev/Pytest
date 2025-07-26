def test_secondary_access_to_fixture(shared_resource):
    assert "tool" in shared_resource
    assert shared_resource["tool"] == "pytest"
