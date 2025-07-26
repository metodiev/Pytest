import pytest
import sys

@pytest.mark.skip(reason="Skipping this test unconditionally")
def test_skip_unconditionally():
    assert 1 == 1

@pytest.mark.skipif(sys.platform == "win32", reason="Skip on Windows")
def test_skip_on_windows():
    assert sys.platform != "win32"

def test_skip_in_code():
    if not sys.platform.startswith("linux"):
        pytest.skip("Skipping test on non-Linux systems")
    assert True
