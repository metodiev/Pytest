# examples/test_example_002_parametrize.py

import pytest

# Test multiple addition cases using parametrize
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),        # simple case
    (2, 3, 5),        # another simple case
    (0, 0, 0),        # edge case with zeros
    (-1, 1, 0),       # positive and negative
])
def test_addition(a, b, expected):
    # Check that a + b equals the expected result
    assert a + b == expected


#  examples/test_example_002_parametrize.py

import pytest

# Test multiple addition cases using parametrize
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),        # simple case
    (2, 3, 5),        # another simple case
    (0, 0, 0),        # edge case with zeros
    (-1, 1, 0),       # positive and negative
])
def test_addition(a, b, expected):
    # Check that a + b equals the expected result
    assert a + b == expected


# Test multiple string uppercases using parametrize
@pytest.mark.parametrize("original, uppercased", [
    ("hello", "HELLO"),
    ("pytest", "PYTEST"),
    ("Test", "TEST"),
])
def test_uppercase(original, uppercased):
    # Check that string.upper() returns expected uppercase
    assert original.upper() == uppercased
#Test multiple string uppercases using parametrize
@pytest.mark.parametrize("original, uppercased", [
    ("hello", "HELLO"),
    ("pytest", "PYTEST"),
    ("Test", "TEST"),
])
def test_uppercase(original, uppercased):
    # Check that string.upper() returns expected uppercase
    assert original.upper() == uppercased
