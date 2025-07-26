def test_using_shared_resource(shared_resource):
    assert shared_resource["tool"] == "pytest"
    assert shared_resource["version"] == "7.0"

def test_using_session_config(session_config):
    assert session_config["env"] == "staging"
    assert not session_config["debug"]
