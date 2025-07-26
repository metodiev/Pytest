"""
test_example_071_using_capfd.py

This test demonstrates using pytest's capfd fixture to capture
stdout and stderr output during test execution.

Usage:
- Run: `pytest -v`
"""

def greet():
    print("Hello, pytest!")

def test_greet_output(capfd):
    greet()
    out, err = capfd.readouterr()
    assert out == "Hello, pytest!\n"
    assert err == ""
