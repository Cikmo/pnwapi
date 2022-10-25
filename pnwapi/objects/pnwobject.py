from abc import ABC, abstractmethod
from typing import TypeVar

PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject")


class PnwObject(ABC):
    """Base class for all PnwObjects."""

    @abstractmethod
    async def _fetch(self):
        pass


class PnwObjectList(tuple[PNWOBJECT]):
    """Represents a list of PnwObjects."""

    def first(self) -> PnwObject | None:
        """Returns the first object.

        Returns:
            The first PnwObject, or None if the list is empty.
        """
        return self[0] if len(self) > 0 else None

    def filter(self, **kwargs) -> "PnwObjectList":
        """Filter the list by the given kwargs.

        args:
            **kwargs: The key-value pairs to filter by.

        Returns:
            A new PnwObjectList containing the filtered objects.
        """
        return PnwObjectList(
            [obj for obj in self if all(
                [getattr(obj, key) == value for key, value in kwargs.items()])])

    def order_by(self, key, reverse=False) -> "PnwObjectList":
        """Sort the list by the given key.

        Args:
            key: The key to sort by.
            reverse: Whether to reverse the order.

        Returns:
            A new PnwObjectList containing the sorted objects.
        """
        return PnwObjectList(sorted(self, key=lambda x: getattr(x, key), reverse=reverse))
