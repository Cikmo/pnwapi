from typing import TYPE_CHECKING

from . import pnwobject, alliance

if TYPE_CHECKING:
    from pnwkit.new import SubscriptionModelLiteral
    from pnwapi import query


class Nation(pnwobject.PnwObject):
    __slots__ = ("id", "name", "alliance")
    _api_name: "SubscriptionModelLiteral" = "nation"

    def __init__(self):
        self.id: int
        self.name: str
        self.alliance: "query.PnwQuerySet[alliance.Alliance]"
