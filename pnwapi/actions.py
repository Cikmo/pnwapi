import asyncio
import typing
import pnwkit

from tortoise.expressions import Q
from .objects import Nation, PnwObjectList


class ActionMeta(type):
    def __call__(self):
        raise RuntimeError(
            f"{self.__name__} is not meant to be instantiated.")

    def __getattribute__(self, attr: str):
        if not attr.startswith("__"):
            if attr in dir(self) and not attr in self.__dict__:
                raise NotImplementedError(
                    f"Action {self.__name__} does not implement {attr} method")

        return super().__getattribute__(attr)


class Action(metaclass=ActionMeta):
    """Base class for all actions."""

    @classmethod
    async def nations(cls):
        pass

    @classmethod
    async def alliances(cls):
        pass

    @classmethod
    async def cities(cls):
        pass

    @classmethod
    async def colors(cls):
        pass

    @classmethod
    async def wars(cls):
        pass

    @classmethod
    async def war_attacks(cls):
        pass

    @classmethod
    async def treaties(cls):
        pass

    @classmethod
    async def trades(cls):
        pass

    @classmethod
    async def trade_prices(cls):
        pass

    @classmethod
    async def bank_records(cls):
        pass

    @classmethod
    async def tax_records(cls):
        pass

    @classmethod
    async def tax_brackets(cls):
        pass

    @classmethod
    async def bounties(cls):
        pass

    @classmethod
    async def treasures(cls):
        pass

    @classmethod
    async def treasure_trades(cls):
        pass

    @classmethod
    async def embargoes(cls):
        pass

    @classmethod
    async def baseball_games(cls):
        pass

    @classmethod
    async def baseball_teams(cls):
        pass

    @classmethod
    async def baseball_players(cls):
        pass


class Fetch(Action):
    """Fetch directly from the PNW API. Returns a """
    @classmethod
    async def nations(cls, **kwargs) -> PnwObjectList[Nation]:
        """Fetch nations directly from the PNW API.

        Args:
            **kwargs: Keyword arguments to pass to the PNW API.
        """
        pass

    @classmethod
    async def alliances(cls):
        pass

    @classmethod
    async def cities(cls):
        pass

    @classmethod
    async def colors(cls):
        pass

    @classmethod
    async def wars(cls):
        pass

    @classmethod
    async def war_attacks(cls):
        pass

    @classmethod
    async def treaties(cls):
        pass

    @classmethod
    async def trades(cls):
        pass

    @classmethod
    async def trade_prices(cls):
        pass

    @classmethod
    async def bank_records(cls):
        pass

    @classmethod
    async def tax_records(cls):
        pass

    @classmethod
    async def tax_brackets(cls):
        pass

    @classmethod
    async def bounties(cls):
        pass

    @classmethod
    async def treasures(cls):
        pass

    @classmethod
    async def treasure_trades(cls):
        pass

    @classmethod
    async def embargoes(cls):
        pass

    @classmethod
    async def baseball_games(cls):
        pass

    @classmethod
    async def baseball_teams(cls):
        pass

    @classmethod
    async def baseball_players(cls):
        pass


async def test():
    fetch = Fetch

    nations = await fetch.nations()

    for nation in nations:
        print(nation.name)
