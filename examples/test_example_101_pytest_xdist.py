import pytest
import time

@pytest.mark.parametrize("seconds", [1, 2, 3])
def test_sleep(seconds):
    """Simulate a test that takes 'seconds' to run."""
    time.sleep(seconds)
    assert seconds > 0
