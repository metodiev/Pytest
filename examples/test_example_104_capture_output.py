def greet(name):
    print(f"Hello, {name}!")

def test_greet(capsys):
    greet("Miro")
    captured = capsys.readouterr()
    assert "Hello, Miro!" in captured.out
