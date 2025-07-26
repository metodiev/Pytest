import pytest

# ----------------------------
# AUTOUSE fixture: global logging setup/teardown
# ----------------------------
@pytest.fixture(autouse=True, scope="module")
def log_test_start_and_end():
    print("\n[Setup] Starting test module")
    yield
    print("[Teardown] Finishing test module")

# ----------------------------
# Yield fixture: database connection mock
# ----------------------------
@pytest.fixture
def db_connection():
    print("Connecting to database...")
    conn = {"connected": True}
    yield conn
    print("Disconnecting from database...")

# ----------------------------
# Parametrized fixture: dynamic input
# ----------------------------
@pytest.fixture(params=["alice", "bob", "carol"])
def user(request):
    return {"username": request.param}

# ----------------------------
# Function: simple login system
# ----------------------------
def login(user, password):
    if not user or not password:
        raise ValueError("Missing credentials")
    if user == "admin" and password == "secret":
        return True
    return False

# ----------------------------
# Tests
# ----------------------------
@pytest.mark.security
@pytest.mark.parametrize("user,password,expected", [
    ("admin", "secret", True),
    ("admin", "wrong", False),
    ("guest", "guest", False),
])
def test_login_logic(user, password, expected):
    assert login(user, password) == expected

def test_login_raises_on_missing_password():
    with pytest.raises(ValueError, match="Missing credentials"):
        login("admin", None)

def test_user_fixture(user):
    assert "username" in user
    assert isinstance(user["username"], str)

def test_db_connection(db_connection):
    assert db_connection["connected"] is True

def test_print_output(capsys):
    print("This is a test message")
    captured = capsys.readouterr()
    assert "test message" in captured.out
