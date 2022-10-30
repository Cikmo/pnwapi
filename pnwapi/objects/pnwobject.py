from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, TypeVar

import pnwkit.data
import pnwkit.new

if TYPE_CHECKING:
    from pnwkit.new import SubscriptionModelLiteral


PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject[Any]")


class PnwSubscription(Generic[PNWOBJECT, pnwkit.new.T]):
    __slots__ = ("_obj", "_dataclass")

    def __init__(self, obj: type[PNWOBJECT], dataclass: type[pnwkit.new.T]):
        self._obj = obj
        self._dataclass = dataclass

    async def create(self, data: pnwkit.new.T) -> None:
        """Create an object in the db with data from the API."""
        await self._obj._create_or_update(data)  # pyright: reportPrivateUsage=false

    async def update(self, data: pnwkit.new.T) -> None:
        """Update an object in the db with data from the API."""
        pass

    async def delete(self, data: pnwkit.new.T) -> None:
        """Delete an object in the db with data from the API."""
        pass


class PnwObject(ABC, Generic[pnwkit.new.T]):
    """Base class for all PnwObjects."""

    __slots__ = ()
    _api_name: "SubscriptionModelLiteral"

    @abstractmethod
    @classmethod
    async def _create_or_update(cls, data: pnwkit.new.T) -> None:
        pass

    @abstractmethod
    @classmethod
    async def _delete(cls, data: pnwkit.new.T) -> None:
        pass
