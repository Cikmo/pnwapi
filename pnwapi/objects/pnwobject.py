from abc import ABC, abstractmethod
from typing import TypeVar

PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject")


class PnwObject(ABC):
    ...


class PnwObjectList(tuple[PNWOBJECT]):

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
        return PnwObjectList(sorted(self, key=lambda x: getattr(x, key), reverse=reverse))
