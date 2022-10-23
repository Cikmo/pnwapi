import pnwapi
import pytest
import logging
import asyncio
import os

from pnwapi import Pnwapi


async def test_testing(caplog: pytest.LogCaptureFixture, logger: logging.Logger):
    caplog.set_level(logging.INFO)
    api_key = os.environ.get("PNW_API_KEY")
    db_url = os.environ.get("DB_URL")

    await Pnwapi.init(db_url, api_key)

    result = await Pnwapi.get.nations(name="norlandia")

    logger.info(result[0].nation_name)

    await Pnwapi.api.aiohttp_session.close()

    assert 1 == 1
