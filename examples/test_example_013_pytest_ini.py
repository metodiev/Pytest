import pytest

"""pytest.ini controls global Pytest settings:
addopts sets default CLI options.
markers documents custom markers (Pytest enforces marker registration)."""

@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(1)
    assert True

@pytest.mark.smoke
def test_basic_smoke():
    assert 1 + 1 == 2
