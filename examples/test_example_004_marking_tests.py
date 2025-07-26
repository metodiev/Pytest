import pytest

@pytest.mark.slow
def test_slow_computation():
    # Simulate a slow test
    import time
    time.sleep(1)
    assert True

@pytest.mark.fast
def test_fast_computation():
    assert 1 + 1 == 2

@pytest.mark.skip(reason="demonstration of skip marker")
def test_skipped():
    assert False
