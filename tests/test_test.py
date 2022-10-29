import pytest
import logging
import asyncio
import os
import pnwapi

# from pympler import asizeof


async def test_testing(caplog: pytest.LogCaptureFixture, logger: logging.Logger):
    caplog.set_level(logging.INFO)

    api_key = os.environ.get("PNW_API_KEY")
    db_url = os.environ.get("DB_URL")

    if api_key is None:
        raise RuntimeError("No API key provided.")
    if db_url is None:
        raise RuntimeError("No database URL provided.")

    await pnwapi.init(db_url, api_key)
    await pnwapi.alliances.sync(id=12345)
    await pnwapi.nations.sync(id=12345)
    # await pnwapi.alliances.subscribe()
    await pnwapi.nations.filter(name="The United States of America").first()

    await pnwapi.nations.subscribe()
    await asyncio.sleep(15)
    logger.info("1")
    await pnwapi.nations.unsubscribe()
    logger.info("2")
    await pnwapi.close_connections()
    logger.info("3")
    assert 1 == 1
