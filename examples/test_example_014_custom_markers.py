import pytest

@pytest.mark.api
def test_api_get_request():
    # Simulate an API GET call
    response = {"status": 200}
    assert response["status"] == 200

@pytest.mark.db
def test_database_insert():
    # Simulate a DB insert operation
    record_inserted = True
    assert record_inserted
