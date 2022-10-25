from abc import ABC, abstractmethod
from typing import TypeVar, Generic, TYPE_CHECKING

if TYPE_CHECKING:
    from .objects import PnwObject

PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject")


class PnwQuerySet(Generic[PNWOBJECT]):
    """Base class for PnwQueries"""

    def __init__(self, obj: type[PNWOBJECT]):
        self.obj = obj

    async def get(self, **kwargs) -> PNWOBJECT:
        """Get the first object matching the given kwargs."""
        return self.obj()

    def filter(self, **kwargs) -> "PnwQuerySet[PNWOBJECT]":
        """Return a new PnwQuerySet filtered by the given kwargs."""
        return self

    def first(self) -> "PnwQuerySetSingle[PNWOBJECT]":
        """Get the first object in the queryset."""
        queryset = PnwQuerySetSingle(self.obj)
        return queryset

    def sort_by(self, key: str, reverse: bool = False) -> "PnwQuerySet[PNWOBJECT]":
        """Sort the results by the given key."""
        return self

    def __await__(self):
        """Return the results of the query."""
        return self._execute().__await__()

    def __aiter__(self) -> "PnwQuerySet[PNWOBJECT]":
        return self

    def __call__(self, **kwargs) -> "PnwQuerySet[PNWOBJECT]":
        """Return a new PnwQuerySet filtered by the given kwargs."""
        return self.filter(**kwargs)

    async def __anext__(self) -> PNWOBJECT:
        yield self.obj()

    async def _execute(self) -> list[PNWOBJECT]:
        """Execute the query and return the results."""
        return [self.obj()]


class PnwQuerySetSingle(Generic[PNWOBJECT]):
    """QuerySet for single objects."""

    def __init__(self, obj: type[PNWOBJECT]):
        self.obj = obj

    def __call__(self, **kwargs) -> "PnwQuerySetSingle[PNWOBJECT]":
        return self

    def __await__(self):
        """Return the results of the query."""
        return self._execute().__await__()

    async def _execute(self) -> PNWOBJECT:
        """Execute the query and return the results."""
        return self.obj()
