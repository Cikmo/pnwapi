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

    nation = await pnwapi.nations.get(name="norlandia")

    alliance = await nation.alliance

    await pnwapi.Pnwapi._api.aiohttp_session.close()

    assert 1 == 1
