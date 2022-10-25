from datetime import datetime
from enum import Enum
import sys
import pytest
import logging
import asyncio
import os
from pympler import asizeof

import pnwapi


async def test_testing(caplog: pytest.LogCaptureFixture, logger: logging.Logger):
    caplog.set_level(logging.INFO)
    api_key = os.environ.get("PNW_API_KEY")
    db_url = os.environ.get("DB_URL")

    # await Pnwapi.init(db_url, api_key)

    # # result = await Pnwapi.get.nations(name="norlandia")

    # # logger.info(result[0].nation_name)

    await pnwapi.init(db_url, api_key)

    nation = await pnwapi.fetch.nations(name="norlandia")

    await pnwapi.Pnwapi._api.aiohttp_session.close()

    assert 1 == 1


class Nation:
    """
    A Nation Object
    TODO: add attributes and methods in docstring
    """

    def __init__(self, **kwargs):
        self.id: int = kwargs.get("id")
        self.alliance_id: int = kwargs.get("alliance_id")

        self.discord_id: int = kwargs.get("discord_id")
        # Verified that the account is owns the nation
        self.verified: bool = kwargs.get("verified")

        # Make these a single attribute.
        self.alliance_position = kwargs.get(
            "alliance_position")  # AlliancePositionEnum
        self.alliance_position_id: int = kwargs.get("alliance_position_id")
        self.alliance_position_info = kwargs.get(
            "alliance_position_info")  # AlliancePosition object
        ###

        self.alliance = kwargs.get("alliance")  # Alliance object
        self.name: str = kwargs.get("name")
        self.leader_name: str = kwargs.get("leader_name")
        self.continent: str = kwargs.get("continent")  # Make enum?
        self.war_policy = kwargs.get("war_policy")  # WarPolicy enum
        self.domestic_policy = kwargs.get(
            "domestic_policy")  # DomesticPolicy enum
        self.color: str = kwargs.get("color")

        # Make a cities attribute where you can do
        # cities.count()
        # for city in cities:
        self.cities_count: int = kwargs.get("cities_count")
        self.cities = kwargs.get("cities")  # List of City objects
        ###

        self.score: float = kwargs.get("score")
        self.update_tz: str = kwargs.get("update_tz")
        self.population: int = kwargs.get("population")
        self.flag: str = kwargs.get("flag")  # URL
        # Make vacation_mode.turns or vacation_mode.datetime?
        self.vacation_mode_turns: int = kwargs.get("vacation_mode_turns")
        self.beige_turns: int = kwargs.get("beige_turns")  # same with this one
        self.espionage_available: bool = kwargs.get("espionage_available")
        self.last_active: datetime = kwargs.get("last_active")
        self.date_created: datetime = kwargs.get(
            "date_created")  # Called date in the API
        self.military = kwargs.get("military")  # Military object
        self.treasure = kwargs.get("treasure")  # Treasure object
        self.wars = kwargs.get("wars")  # List of War objects

        # List of BankRecord objects (dont save in database, only get on request)
        self.bank_records = kwargs.get("bank_records")
        # List of Trade objects (dont save in database, only get on request)
        self.trades = kwargs.get("trades")
        # List of TaxRecord objects (dont save in database, only get on request)
        self.tax_records = kwargs.get("tax_records")

        self.bounties = kwargs.get("bounties")  # List of Bounty objects
        self.turns_since_last_city = kwargs.get("turns_since_last_city")
        self.turns_since_last_project = kwargs.get("turns_since_last_project")
        self.stockpile = kwargs.get("stockpile")  # Stockpile object
        self.projects = kwargs.get("projects")

        self.tax_id: int = kwargs.get("tax_id")
        self.alliance_seniority: int = kwargs.get("alliance_seniority")
        # BaseballTeam object (dont save in database, only get on request)
        self.baseball_team = kwargs.get("baseball_team")

        self.statsistics = kwargs.get("statistics")  # Statistics object

    def __str__(self):
        return f"{self.name} ({self.id}) - {'Not Verified' if not self.verified else f'Verified with discord id {self.discord_id}'}"


async def main():
    await pnwapi.init("postgres://postgres:postgres@localhost:5432/pnwapi", "API_KEY")

    nation = await pnwapi.nations.filter(name="norlandia").first()

    print(nation.name)

    # OR

    async for nation in pnwapi.nations.filter(alliance="blah"):
        print(nation.name)
