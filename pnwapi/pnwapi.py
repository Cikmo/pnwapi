import asyncio
import os
import pnwkit
import sys
import logging
import pnwkit.errors
import tortoise.exceptions
import pytest

from tortoise import Tortoise
from typing import Generic

from . import exceptions
from . import query
from . import objects

logger = logging.getLogger(__name__)


class Interface(Generic[objects.PNWOBJECT]):
    """The main entry interface for interacting with the library."""
    __slots__ = ("_obj", "_base_query", "filter", "get")

    def __init__(self, obj: type[objects.PNWOBJECT]):
        self._obj = obj
        self._base_query = query.PnwQuerySet(obj)
        self.filter = self._base_query.filter
        self.get = self._base_query.get

    @classmethod
    async def sync(self, return_updated: bool = False, **kwargs) -> list[objects.Alliance] | None:
        """Update the local database with the data from the API.

        args:
            return_updated: Whether to return the updated objects.
            **kwargs: The kwargs to filter the query by.

        Returns:
            Optionally returns a list of the updated objects.
        """
        pass

    @classmethod
    async def subscribe(self, **kwargs) -> None:
        """Subscribe to the API for updates on the given objects. This will watch for changes to the objects and update the local database,
        create new objects and remove deleted ones all automatically.

        This is a non-blocking function. It will return immediately and run in the background. To stop the subscription,
        call the `unsubscribe` method.
        """
        # return an awaitable class. The class will also have a method to unsubscribe.
        # syntax: await pnwapi.alliances.subscribe()
        # set to an object that can be used to unsubscribe.
        pass


class PnwapiMeta(type):
    def __call__(self):
        raise RuntimeError(
            f"{self.__name__} is not meant to be instantiated.")


class Pnwapi(metaclass=PnwapiMeta):
    """
    The Pnwapi class is the main interface for pnwapi. It is a singleton class, and as such, cannot be instantiated.

    Use :meth:`Pnwapi.init` to initialize the class.
    """
    _inited: bool = False
    _api: pnwkit.QueryKit

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

        cls._api = pnwkit.QueryKit(pnw_api_key, pnw_bot_key)

        # test the API key
        query = cls._api.query(
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
        """Internal method to initialize Tortoise ORM. Creates a connection pool to the database, 
        and creates the database tables if they don't exist.

        Args:
            db_url: The connection string for the database.

        Raises:
            exceptions.InvalidDatabaseUrl: Raised when an invalid database URL is provided.
            exceptions.DatabaseConnectionError: Raised when a database connection error occurs.
        """
        # TODO: add support for injection / manual initialization of Tortoise, so that users can use their own Tortoise databases.

        if not "PYTEST_CURRENT_TEST" in os.environ:
            # Tests use a seperate initializer found in the `tests/fixtures.py` file.
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
