import pytest

# Define a fixture that returns a sample dictionary
@pytest.fixture
def sample_data():
    return {"name": "Pesho", "age": 21}

def test_sample_data_name(sample_data):
    assert sample_data["name"] == "Pesho"

def test_sample_data_age(sample_data):
    assert sample_data["age"] == 21
