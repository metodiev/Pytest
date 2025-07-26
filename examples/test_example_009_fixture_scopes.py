import pytest

@pytest.fixture(scope="function")  # Default scope, runs once per test
def function_scope():
    print("\nSetup function_scope")
    yield
    print("Teardown function_scope")

@pytest.fixture(scope="module")  # Runs once per module (all tests in this file)
def module_scope():
    print("\nSetup module_scope")
    yield
    print("Teardown module_scope")

@pytest.fixture(scope="session")  # Runs once per test session
def session_scope():
    print("\nSetup session_scope")
    yield
    print("Teardown session_scope")

def test_func1(function_scope, module_scope, session_scope):
    assert True

def test_func2(function_scope, module_scope, session_scope):
    assert True
