import pytest
import logging
import asyncio

from pnwapi import Pnwapi


async def test_testing(caplog: pytest.LogCaptureFixture, logger: logging.Logger):
    caplog.set_level(logging.INFO)
    logger.info("This is a test")
    #pnw = Pnwapi.init()
    assert 1 == 1


def test_argh(logger: logging.Logger):
    logger.info("This is a test umber 2")
    logger.warning("This is a warning test")
    assert 1 == 1
