# examples/test_example_001_basic_assert.py

def test_basic_addition():
    assert 1 + 1 == 2

def test_string_comparison():
    assert "hello".upper() == "HELLO"

def test_membership():
    # Check that 3 is present in the list
    """Ensure that 3 is an element in the sample list."""
    assert 3 in [1, 2, 3, 4]
