import pytest

@pytest.fixture(scope="module")
def module_resource():
    print("\n[setup] Module-level resource")
    yield "module data"
    print("[teardown] Module-level resource")

@pytest.fixture(scope="session")
def session_resource():
    print("\n[setup] Session-level resource")
    yield "session data"
    print("[teardown] Session-level resource")

def test_using_module_resource(module_resource):
    print("Using:", module_resource)
    assert module_resource == "module data"

def test_using_session_resource(session_resource):
    print("Using:", session_resource)
    assert session_resource == "session data"
