from datetime import datetime
from enum import Enum
import sys
import pytest
import logging
import asyncio
import os
from pympler import asizeof
import pnwapi


async def test_testing(caplog: pytest.LogCaptureFixture, logger: logging.Logger):
    caplog.set_level(logging.INFO)
    api_key = os.environ.get("PNW_API_KEY")
    db_url = os.environ.get("DB_URL")

    await pnwapi.init(db_url, api_key)
    await pnwapi.alliances.sync(id=12345)
    await pnwapi.nations.sync(id=12345)
    await pnwapi.alliances.subscribe()
    await pnwapi.nations.filter(name="The United States of America").first()
    await pnwapi.close_connections()
    assert 1 == 1
