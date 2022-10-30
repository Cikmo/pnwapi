from typing import TYPE_CHECKING

from . import pnwobject, alliance
from pnwapi import pnwapi
import pnwkit.data
import pnwkit.new

if TYPE_CHECKING:
    from pnwapi import query


class Nation(pnwobject.PnwObject[pnwkit.data.Nation]):
    __slots__ = ("id", "name", "alliance", "_dataclass")
    _api_name = "nation"

    def __init__(self):
        self.id: int
        self.name: str
        self.alliance: "query.PnwQuerySet[alliance.Alliance]"

    @classmethod
    async def _create_or_update(cls, data: pnwkit.data.Nation) -> None:
        pnwapi.logger.info("Updating nation %s", data.nation_name)
        pass

    @classmethod
    async def _delete(cls, data: pnwkit.data.Nation) -> None:
        pass
