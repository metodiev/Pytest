"""
test_example_024_async_testing.py

This test module demonstrates asynchronous test functions using pytest-asyncio.

Requirements:
- Install pytest-asyncio: `pip install pytest-asyncio`

Markers:
- @pytest.mark.asyncio: Marks a test function as async

Tests:
- Simulate an async data fetch
- Validate awaitable logic

Usage:
- Run: `pytest -v`
"""

import pytest
import asyncio

async def fake_fetch_data(delay: float = 0.1):
    await asyncio.sleep(delay)
    return {"status": 200, "data": [1, 2, 3]}

@pytest.mark.asyncio
async def test_async_fetch_success():
    result = await fake_fetch_data()
    assert result["status"] == 200
    assert len(result["data"]) == 3

@pytest.mark.asyncio
async def test_async_fetch_timeout():
    result = await fake_fetch_data(0.05)
    assert isinstance(result, dict)
