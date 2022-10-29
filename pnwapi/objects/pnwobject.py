from abc import ABC, abstractmethod
from typing import TypeVar, TYPE_CHECKING, Any
import pnwkit.data

if TYPE_CHECKING:
    from pnwkit.new import SubscriptionModelLiteral


PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject")


class PnwObject(ABC):
    """Base class for all PnwObjects."""

    __slots__ = ()
    _api_name: "SubscriptionModelLiteral"
    _api_dataclass: type[pnwkit.data.Data]

    @classmethod
    @abstractmethod
    async def _update(cls, data: Any) -> None:
        """Update an object in the db with data from the API."""
        pass

    @classmethod
    @abstractmethod
    async def _create(cls, data: Any) -> None:
        """Create an object in the db with data from the API."""
        pass

    @classmethod
    @abstractmethod
    async def _delete(cls, data: Any) -> None:
        """Delete an object in the db with data from the API."""
        pass
