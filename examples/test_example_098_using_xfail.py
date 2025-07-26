import pytest

@pytest.mark.xfail(reason="Feature not implemented yet")
def test_feature_not_ready():
    assert False  # This test is expected to fail

@pytest.mark.xfail(strict=True, reason="Known bug")
def test_known_bug():
    # This test must fail, otherwise pytest marks it as failure
    assert 1 + 1 == 3
