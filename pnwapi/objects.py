from typing import TypeVar, Generic
from pnwapi.query import PnwQuerySet


class PnwObject:
    """Base class for all PnwObjects."""
    __slots__ = ()


class Nation(PnwObject):
    __slots__ = ("id", "name", "alliance")

    def __init__(self):
        self.id: int
        self.name: str
        self.alliance = PnwQuerySet(Alliance).first()


class Alliance(PnwObject):
    __slots__ = ("id", "name", "members")

    def __init__(self):
        self.id: int
        self.name: str
        self.members = PnwQuerySet(Nation)
