import asyncio
import os
import pnwkit
import sys
import logging

from tortoise import Tortoise
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class Pnwapi:
    """
    The Pnwapi class is a singleton class that is used to initialize the pnwapi library.
    """
    _inited: bool = False

    api_key: str
    bot_key: str | None = None
    db_url: str

    api: pnwkit.QueryKit

    def __init__(self):
        # If a class instance is attempted to be created, raise an error.
        raise RuntimeError(
            "Pnwapi cannot be instantiated as an instance. Use Pnwapi.init() instead.")

    @classmethod
    async def _init(cls, db_url: str,
                    pnw_api_key: str,
                    pnw_bot_key: str = None) -> None:

        # Only initialize the DB if we're not in a test environment.
        # Tests use a seperate initializer found in the `tests/fixtures.py` file.
        if not "pytest" in sys.modules:
            logger.warning(
                "If this is a test, you shouldn't see this message. You can safely ignore this warning if this is not a test. This warning is located in pnwapi.py in the Pnwapi.init() function.")
            tortoise_config = {
                'connections': {
                    'default': db_url
                },
                'apps': {
                    'pnwapi': {
                        'models': ['pnwapi.models'],
                        'default_connection': 'default',
                    }
                },
                'use_tz': False,
                'timezone': 'UTC'
            }

            await Tortoise.init(config=tortoise_config)
            await Tortoise.generate_schemas()

        else:
            logger.warning(
                "This is a test environment. Skipping DB initialization.")

        cls.api_key = pnw_api_key
        cls.bot_key = pnw_bot_key
        cls.db_url = db_url
        cls.api = pnwkit.QueryKit(pnw_api_key, pnw_bot_key)

        cls._inited = True


async def init(db_url: str,
               pnw_api_key: str,
               pnw_bot_key: str = None) -> None:
    """
    Initialize pnwapi. This creates a singleton instance of the Pnw class, which can be accessed via the pnwapi.Pnw object.

    Args:
        db_url: The connection string for the database. See https://tortoise-orm.readthedocs.io/en/latest/databases.html#db-url for more information.
        pnw_api_key: The PnW API key to use for API requests.
        pnw_bot_key: The PnW bot key needed for certain PUT API requests. Defaults to None.
    """
    await Pnwapi._init(db_url, pnw_api_key, pnw_bot_key)
