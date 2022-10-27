from typing import TypeVar, Generic
from pnwapi import query
from . import pnwobject, alliance


class Nation(pnwobject.PnwObject):
    __slots__ = ("id", "name", "alliance")

    def __init__(self):
        self.id: int
        self.name: str
        self.alliance = query.PnwQuerySet(
            alliance.Alliance).first()
