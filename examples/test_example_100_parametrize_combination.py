import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30),
])
def test_addition(a, b, expected):
    assert a + b == expected
