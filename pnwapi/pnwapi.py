import asyncio
import os
import pnwkit
import sys
import logging
import pnwkit.errors
import tortoise.exceptions
import pytest

from . import exceptions

from tortoise import Tortoise
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class Get:
    @classmethod
    async def nations(self, name: str):
        query = await Pnwapi.api.query("nations", {"nation_name": name, "first": 1}, "nation_name")

        return query.nations


class Pnwapi:
    """
    The Pnwapi class is the main interface for pnwapi. It is a singleton class, and as such, cannot be instantiated.

    Use :meth:`Pnwapi.init` to initialize the class.
    """
    _inited: bool = False

    api: pnwkit.QueryKit

    get: Get = Get

    def __init__(self):
        # Note: This class cannot be instantiated, as it is a singleton. All methods are classmethods.
        # If a class instance is attempted to be created, raise an error.
        raise RuntimeError(
            "Pnwapi cannot be instantiated as an instance. Use Pnwapi.init() instead.")

    @classmethod
    async def init(cls, db_url: str,
                   pnw_api_key: str,
                   pnw_bot_key: str = None) -> None:
        """
        Initialize pnwapi.

        Args:
            db_url: The connection string for the database. See https://tortoise.github.io/databases.html#db-url for more information.
            pnw_api_key: The PnW API key to use for API requests.
            pnw_bot_key: The PnW bot key needed for certain PUT API requests. Defaults to None.

        Raises:
            AlreadyInitializedError: Raised when Pnwapi.init() is called more than once.
        """
        if cls._inited:
            raise exceptions.AlreadyInitializedError(
                "Pnwapi has already been initialized.")

        await cls._db_init(db_url)

        cls.api = pnwkit.QueryKit(pnw_api_key, pnw_bot_key)

        # test the API key
        query = cls.api.query(
            "nations", {"id": 239259, "first": 1}, "nation_name")
        try:
            await query.get_async()
        except pnwkit.errors.GraphQLError as e:
            if str(e).startswith("You specified an invalid api_key."):
                raise exceptions.InvalidApiKeyError(
                    "The provided API key is invalid. Please check your API key and try again.")
            else:
                raise

        cls._inited = True

    @classmethod
    async def _db_init(cls, db_url: str) -> None:
        # Only initialize the DB if we're not in a test environment.
        # Tests use a seperate initializer found in the `tests/fixtures.py` file.
        if not "PYTEST_CURRENT_TEST" in os.environ:
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

            try:
                await Tortoise.init(config=tortoise_config)
                await Tortoise.generate_schemas()
            except tortoise.exceptions.ConfigurationError as e:
                if "Unknown DB scheme" in str(e):
                    raise exceptions.InvalidDatabaseUrl(
                        "The database URL schema provided is invalid.")
                raise
            except OSError as e:
                if "[Errno 10061]" in str(e):
                    raise exceptions.DatabaseConnectionError(
                        "Could not connect to the database. Is the database running?")
                raise
            except:
                raise

        else:
            logger.warning(
                "If this is not a test, you shouldn't see this message. Skipping DB initialization.")

    @staticmethod
    def _enforce_init(func):
        """Decorator that enforces that the class has been initialized before calling the function.

        Raises:
            NotInitializedError: If the class has not been initialized.
        """
        def wrapper(*args, **kwargs):
            if not Pnwapi._inited:
                raise exceptions.NotInitializedError(
                    "Pnwapi has not been initialized. Please call Pnwapi.init() before using the library.")
            return func(*args, **kwargs)
        return wrapper
