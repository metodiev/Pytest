def test_create_file_in_tmpdir(tmpdir):
    # Create a new file in the temporary directory
    file = tmpdir.join("hello.txt")
    file.write("Hello from tmpdir!")

    # Read the file content and verify
    content = file.read()
    assert content == "Hello from tmpdir!"

def test_tmpdir_starts_empty(tmpdir):
    # tmpdir should be empty at the start of each test
    assert len(tmpdir.listdir()) == 0
