from typing import TYPE_CHECKING

from . import pnwobject, nation

if TYPE_CHECKING:
    from pnwkit.new import SubscriptionModelLiteral
    from pnwapi import query


class Alliance(pnwobject.PnwObject):
    __slots__ = ("id", "name", "members")
    _api_name: "SubscriptionModelLiteral" = "alliance"

    def __init__(self):
        self.id: int
        self.name: str
        self.members: "query.PnwQuerySet[nation.Nation]"
