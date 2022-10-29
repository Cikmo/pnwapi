from typing import TYPE_CHECKING

from . import pnwobject, alliance
from pnwapi import pnwapi
import pnwkit.data

if TYPE_CHECKING:
    from pnwapi import query


class Nation(pnwobject.PnwObject):
    __slots__ = ("id", "name", "alliance")
    _api_name = "nation"
    _api_dataclass = pnwkit.data.Nation

    def __init__(self):
        self.id: int
        self.name: str
        self.alliance: "query.PnwQuerySet[alliance.Alliance]"

    @classmethod
    async def _update(cls, data: pnwkit.data.Nation) -> None:
        pnwapi.logger.info(data.nation_name)
        pass

    @classmethod
    async def _create(cls, data: pnwkit.data.Nation) -> None:
        pass

    @classmethod
    async def _delete(cls, data: pnwkit.data.Nation) -> None:
        pass
