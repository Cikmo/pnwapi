import logging
import pytest
import os
import asyncio
import platform
import asyncpg

from tortoise.contrib.test import finalizer, initializer
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError, OperationalError

log = logging.getLogger(__package__)


@pytest.fixture
def logger():
    return log


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request: pytest.FixtureRequest):
    log.debug("Initializing test Tortoise-ORM database.")
    db_url = os.environ.get("DB_URL", "sqlite://:memory:")
    initializer(["tests.testmodels"],
                db_url=db_url, app_label="pnwapi")
    request.addfinalizer(finalizer)
    log.debug("Test Tortoise-ORM database initialized.")


@pytest.fixture(scope='session')
def event_loop():
    # A fix for a bug where on Windows, a 'RuntimeError: Event loop is closed' is raised.
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
