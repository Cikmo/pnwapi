from typing import TypeVar, Generic
from pnwapi.query import PnwQuerySet


class PnwObject:
    """Base class for all PnwObjects."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Nation(PnwObject):
    __slots__ = ("id", "name", "alliance")

    def __init__(self):
        self.id: int
        self.name: str
        self.alliance = PnwQuerySet(Alliance).first()


class Alliance(PnwObject):
    __slots__ = ("id", "name")

    def __init__(self):
        self.id: int
        self.name: str
        self.members = PnwQuerySet(Nation)
