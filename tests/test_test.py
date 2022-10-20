import pnwapi
import pytest
import logging
import asyncio
import os

import pnwapi


async def test_testing(caplog: pytest.LogCaptureFixture, logger: logging.Logger):
    caplog.set_level(logging.INFO)
    api_key = os.environ.get("PNW_API_KEY")
    db_url = os.environ.get("DB_URL")

    await pnwapi.init(db_url, api_key)

    assert 1 == 1
