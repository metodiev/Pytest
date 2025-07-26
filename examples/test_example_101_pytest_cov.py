"""How to run the report: pytest --html=report.html --self-contained-html test_example_102_pytest_html.py
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
