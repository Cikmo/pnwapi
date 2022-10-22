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
    db_url = os.environ.get("DB_URL", "sqlite://:memory:")

    failed = False
    while True:
        try:
            log.debug("Initializing test Tortoise-ORM.")
            initializer(["tests.testmodels"],
                        db_url=db_url, app_label="pnwapi")
            request.addfinalizer(finalizer)
        except:
            if failed is False and db_url != "sqlite://:memory:":
                log.warning(
                    "Failed to initialize Tortoise-ORM using the DB_URL environment variable. Falling back to sqlite://:memory:.")
                failed = True
                db_url = "sqlite://:memory:"
                continue
            else:
                log.error(
                    f"Failed to initialize Tortoise-ORM using {db_url}.")
                raise
        break


@pytest.fixture(scope='session')
def event_loop():
    # A fix for a bug where on Windows, a 'RuntimeError: Event loop is closed' is raised.
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
