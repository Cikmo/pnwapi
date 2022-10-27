from typing import TypeVar, Generic
from pnwapi import query
from . import pnwobject, nation


class Alliance(pnwobject.PnwObject):
    #__slots__ = ("id", "name", "members")
    _api_name: str = "alliance"

    def __init__(self):
        self.id: int
        self.name: str
        self.members = query.PnwQuerySet(nation.Nation).filter()
