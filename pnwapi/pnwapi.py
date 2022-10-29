import os
import logging
import pnwkit
import pnwkit.errors
import tortoise.exceptions

from tortoise import Tortoise
from typing import Generic, Any, Callable, TYPE_CHECKING

from . import exceptions
from . import query

from . import objects

if TYPE_CHECKING:
    import pnwkit.new
    import pnwkit.data
logger = logging.getLogger(__name__)


def _raise_if_not_inited(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that checks if Pnwapi has been initialized before calling the function.

    Raises:
        NotInitializedError: If Pnwapi has not been initialized.
    """

    def wrapper(*args: Any, **kwargs: Any):
        if not Pnwapi._inited:
            raise exceptions.NotInitializedError(
                "Pnwapi has not been initialized. Please call Pnwapi.init() before using the library."
            )
        return func(*args, **kwargs)

    return wrapper


class Interface(Generic[objects.PNWOBJECT]):
    """The main entry interface for interacting with the library."""

    __slots__ = ("_obj", "_base_query", "_subscription", "filter", "get")

    def __init__(self, obj: type[objects.PNWOBJECT]):
        self._obj = obj
        self._base_query = query.PnwQuerySet(obj)
        self._subscription: pnwkit.Subscription[Any] | None = None

        self.filter = self._base_query.filter
        self.get = self._base_query.get

    @_raise_if_not_inited
    async def sync(
        self, return_updated: bool = False, **kwargs: str
    ) -> list[objects.PNWOBJECT] | None:
        """Update the local database with the data from the API.

        args:
            return_updated: Whether to return the updated objects.
            **kwargs: The kwargs to filter the query by.

        Returns:
            Optionally returns a list of the updated objects.
        """
        pass

    @_raise_if_not_inited
    async def subscribe(self) -> None:
        """Subscribe to the API for updates on the given objects. This will watch for changes to the objects and update the local database,
        create new objects and remove deleted ones all automatically.

        This is a non-blocking function. It will return immediately and run in the background. To stop the subscription,
        call the `unsubscribe` method.
        """
        self._subscription = await Pnwapi.api.subscribe(
            self._obj._api_name, "update", None, self._subscription_update_callback
        )  # pyright: reportPrivateUsage=false

    @_raise_if_not_inited
    async def unsubscribe(self) -> None:
        """Unsubscribe from the API for updates on the given object, if a subscription exists."""
        if self._subscription is not None:
            await self._subscription.unsubscribe()
            self._subscription = None

    @_raise_if_not_inited
    async def raw_request(self, endpoint: str, **kwargs: str) -> dict[str, Any]:
        """Make a raw request to the API.

        args:
            endpoint: The endpoint to make the request to.
            **kwargs: The kwargs to pass to the request.

        Returns:
            The response from the API.
        """
        ...

    async def _subscription_update_callback(self, data: "pnwkit.data.Data") -> None:
        """Callback for update events from subscriptions."""
        await self._obj._update(data)

    async def _subscription_create_callback(self, data: "pnwkit.data.Data") -> None:
        """Callback for create events from subscriptions."""
        await self._obj._create(data)

    async def _subscription_delete_callback(self, data: "pnwkit.data.Data") -> None:
        """Callback for delete events from subscriptions."""
        await self._obj._delete(data)


class PnwapiMeta(type):
    def __call__(self, *args: Any, **kwargs: Any):
        raise RuntimeError(f"{self.__name__} is not meant to be instantiated.")


class Pnwapi(metaclass=PnwapiMeta):
    """
    The Pnwapi class is the main interface for pnwapi. It is a singleton class, and as such, cannot be instantiated.

    Use :meth:`Pnwapi.init` to initialize the class.
    """

    _inited: bool = False
    api: pnwkit.QueryKit

    @classmethod
    async def init(
        cls, db_url: str, pnw_api_key: str, pnw_bot_key: str | None = None
    ) -> None:
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
                "Pnwapi has already been initialized."
            )

        await cls._db_init(db_url)

        cls.api = pnwkit.QueryKit(pnw_api_key, pnw_bot_key)

        # test the API key
        query = cls.api.query("nations", {"id": 239259, "first": 1}, "nation_name")
        try:
            await query.get_async()
        except pnwkit.errors.GraphQLError as e:
            if str(e).startswith("You specified an invalid api_key."):
                raise exceptions.InvalidApiKeyError(
                    "The provided API key is invalid. Please check your API key and try again."
                )
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
                "If this is a test, you shouldn't see this message. You can safely ignore this warning if this is not a test. This warning is located in pnwapi.py in the Pnwapi.init() function."
            )
            tortoise_config = {
                "connections": {"default": db_url},
                "apps": {
                    "pnwapi": {
                        "models": ["pnwapi.models"],
                        "default_connection": "default",
                    }
                },
                "use_tz": False,
                "timezone": "UTC",
            }

            try:
                await Tortoise.init(config=tortoise_config)  # type: ignore
                await Tortoise.generate_schemas()
            except tortoise.exceptions.ConfigurationError as e:
                if "Unknown DB scheme" in str(e):
                    raise exceptions.InvalidDatabaseUrl(
                        "The database URL schema provided is invalid."
                    )
                raise
            except OSError as e:
                if "[Errno 10061]" in str(e):
                    raise exceptions.DatabaseConnectionError(
                        "Could not connect to the database. Is the database running?"
                    )
                raise
            except:
                raise

        else:
            logger.warning(
                "If this is not a test, you shouldn't see this message. Skipping DB initialization."
            )
