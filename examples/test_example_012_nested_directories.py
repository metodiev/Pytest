
import pytest

import pytest

@pytest.fixture
def global_config():
    return {
        "setting": "value",
        "env": "testing",   # Add this key
        "debug": True  # <-- Add this key
    }

# @pytest.fixture
# def global_config():
#     # Setup code for your global config
#     return {"setting": "value"}

def test_nested_access_to_shared_fixture(global_config):
    assert isinstance(global_config, dict)
    assert global_config["env"] == "testing"
    assert global_config["debug"] is True
