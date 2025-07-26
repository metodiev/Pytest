"""
test_example_041_capturing_output.py

This test module demonstrates capturing stdout and stderr using pytest's capfd fixture.

Tests:
- Capture printed output and assert its content

Usage:
- Run: `pytest -v`
"""

def greet():
    print("Hello, World!")

def warn():
    import sys
    print("Warning: something happened!", file=sys.stderr)

def test_greet_output(capfd):
    greet()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n"
    assert err == ""

def test_warn_output(capfd):
    warn()
    out, err = capfd.readouterr()
    assert out == ""
    assert "Warning" in err
