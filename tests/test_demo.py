import asyncio

import pytest


async def get_status_code():
    await asyncio.sleep(10)
    return 200


pytestmark = pytest.mark.asyncio


class TestDemo:
    async def test_demo(self):
        assert 200 == await get_status_code()
