import pytest
import time

#pytest -n 3 test_example_103_pytest_xdist.py

@pytest.mark.parametrize("seconds", [1, 2, 3])
def test_sleep(seconds):
    """Simulates a test that takes 'seconds' seconds to run."""
    time.sleep(seconds)
    assert seconds > 0
