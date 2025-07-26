"""
test_example_055_mocking_datetime_with_freezegun.py

This test module shows how to use freezegun to freeze time in tests.

Usage:
- Install freezegun: `pip install freezegun`
- Run: `pytest -v`
"""

from datetime import datetime
from freezegun import freeze_time

def get_current_time():
    return datetime.now()

@freeze_time("2024-01-01 12:00:00")
def test_time_is_frozen():
    now = get_current_time()
    assert now.year == 2024
    assert now.month == 1
    assert now.day == 1
    assert now.hour == 12
    assert now.minute == 0
