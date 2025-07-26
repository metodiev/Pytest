import pytest

@pytest.fixture
def shared_resource():
    return {"tool": "pytest", "version": "7.0"}

@pytest.fixture(scope="session")
def session_config():
    return {"env": "staging", "debug": False}

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev / staging / prod",
    )

@pytest.fixture
def shared_data():
    return {"framework": "pytest", "language": "Python"}


@pytest.fixture
def sample_data():
    return {"name": "Test", "age": 300}