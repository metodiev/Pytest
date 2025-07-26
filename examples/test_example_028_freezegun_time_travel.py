"""
test_example_028_freezegun_time_travel.py

This test module demonstrates freezing time using the freezegun library.

Requirements:
- Install freezegun: `pip install freezegun`

Tests:
- Freeze time at a specific date and verify behavior.

Usage:
- Run: `pytest -v`

What is Freezegun?
Freezegun is a Python library that “freezes” the system time so that your code behaves as if the current time is fixed at a specific moment. 
This lets you test scenarios involving dates and times reliably without waiting or fiddling with actual system clocks.

Why use Freezegun?
Make time-dependent tests deterministic: Tests relying on datetime.now() or time.time() can be flaky or hard to reproduce.
Freezegun eliminates that by freezing time.
Test expiry and scheduling logic: For example, subscriptions, token expiration, scheduled jobs.
Simulate past/future dates: You can test how your app behaves on specific dates like holidays, deadlines, or leap years.
Avoid system clock hacks: You don't have to change your machine's clock or mock datetime objects manually.
"""

from freezegun import freeze_time
from datetime import datetime

def get_current_year():
    return datetime.now().year

@freeze_time("2020-01-01")
def test_frozen_time():
    assert get_current_year() == 2020

@freeze_time("1999-12-31")
def test_another_frozen_time():
    assert get_current_year() == 1999
