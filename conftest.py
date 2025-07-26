import pytest

@pytest.fixture
def shared_resource():
    return {"tool": "pytest", "version": "7.0"}

@pytest.fixture(scope="session")
def session_config():
    return {"env": "staging", "debug": False}
