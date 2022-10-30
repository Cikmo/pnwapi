from typing import TYPE_CHECKING

from . import pnwobject, nation
import pnwkit.data

if TYPE_CHECKING:
    from pnwkit.new import SubscriptionModelLiteral
    from pnwapi import query


class Alliance(pnwobject.PnwObject[pnwkit.data.Alliance]):
    __slots__ = ("id", "name", "members")
    _api_name: "SubscriptionModelLiteral" = "alliance"

    def __init__(self):
        self.id: int
        self.name: str
        self.members: "query.PnwQuerySet[nation.Nation]"

    @classmethod
    async def _create_or_update(cls, data: pnwkit.data.Alliance) -> None:
        pass

    @classmethod
    async def _delete(cls, data: pnwkit.data.Alliance) -> None:
        pass
