import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    # Check that dividing by zero raises a ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_value_error():
    # Check that ValueError is raised with invalid int conversion
    with pytest.raises(ValueError):
        int("not_an_int")
