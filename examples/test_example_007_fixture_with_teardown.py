import pytest

@pytest.fixture
def resource():
    # Setup code
    print("Setting up resource")
    resource_data = {"connected": True}
    """yield is a keyword used inside a function to make it a generator. 
    yield is a keyword used inside a function to make it a generator.
    When a function uses yield, it pauses execution and sends a value back to the caller.
    Later, it resumes where it left off when called again.When a function uses yield, it pauses execution and sends a value back to the caller.
    Later, it resumes where it left off when called again.
    | `return`                  | `yield`                              |
    | ------------------------- | ------------------------------------ |
    | Exits the function        | Pauses function, keeps state         |
    | Sends one value           | Sends a sequence of values over time |
    | Function produces a value | Function produces a generator        |
    
    Why use yield in fixtures?
    Allows clean separation of setup and teardown in one fixture function.
    Avoids the need for multiple functions or complex try/finally blocks.
    Makes tests cleaner and easier to manage.
    """
    yield resource_data
    # Teardown code
    print("Tearing down resource")
    resource_data["connected"] = False

def test_resource_connection(resource):
    assert resource["connected"] is True
