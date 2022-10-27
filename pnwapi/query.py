from typing import Generic
from . import objects


class PnwQuerySet(Generic[objects.PNWOBJECT]):
    """Base class for PnwQueries"""
    __slots__ = ("_obj",)

    def __init__(self, obj: type[objects.PNWOBJECT]):
        self._obj = obj

    async def get(self, **kwargs) -> objects.PNWOBJECT:
        """Get the first object matching the given kwargs."""
        return self._obj()

    def filter(self, **kwargs) -> "PnwQuerySet[objects.PNWOBJECT]":
        """Return a new PnwQuerySet filtered by the given kwargs."""
        return self

    def first(self, **kwargs) -> "PnwQuerySetSingle[objects.PNWOBJECT]":
        """Get the first object in the queryset."""
        queryset = PnwQuerySetSingle(self._obj)
        return queryset

    def sort_by(self, key: str, reverse: bool = False) -> "PnwQuerySet[objects.PNWOBJECT]":
        """Sort the results by the given key."""
        return self

    def __await__(self):
        """Return the results of the query."""
        return self._execute().__await__()

    def __aiter__(self) -> "PnwQuerySet[objects.PNWOBJECT]":
        return self

    def __call__(self, **kwargs) -> "PnwQuerySet[objects.PNWOBJECT]":
        """Return a new PnwQuerySet filtered by the given kwargs."""
        return self.filter(**kwargs)

    async def __anext__(self) -> objects.PNWOBJECT:
        yield self._obj()

    async def _execute(self) -> list[objects.PNWOBJECT]:
        """Execute the query and return the results."""
        return self._obj()


class PnwQuerySetSingle(Generic[objects.PNWOBJECT]):
    """QuerySet for single objects."""
    __slots__ = ("_obj",)

    def __init__(self, obj: type[objects.PNWOBJECT]):
        self._obj = obj

    def __call__(self, **kwargs) -> "PnwQuerySetSingle[objects.PNWOBJECT]":
        return self

    def __await__(self):
        """Return the results of the query."""
        return self._execute().__await__()

    async def _execute(self) -> objects.PNWOBJECT:
        """Execute the query and return the results."""
        return self._obj()
