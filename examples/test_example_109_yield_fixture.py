import pytest

@pytest.fixture
def open_file():
    print("\n[setup] Opening file")
    f = open("test_temp.txt", "w")
    yield f
    print("[teardown] Closing file")
    f.close()

def test_write_file(open_file):
    open_file.write("Hello, pytest!")
    open_file.flush()
    assert not open_file.closed
