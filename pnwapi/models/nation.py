import typing
from . import model_enums

from tortoise.models import Model
from tortoise import fields, expressions
from tortoise.queryset import QuerySet

if typing.TYPE_CHECKING:
    from . import (
        CityModel,
        AllianceModel,
        TaxBracketModel,
        AlliancePositionModel,
        ColorModel,
        WarModel,
        BankRecordModel,
        TaxRecordModel,
        TreasureModel
    )


class NationModel(Model):
    """Represents a nation."""
    id = fields.IntField(pk=True)
    name = fields.TextField()
    discord_id = fields.BigIntField(null=True, default=None)
    discord_name_pnw = fields.CharField(null=True, default=None, max_length=1)
    leader_name = fields.TextField()
    continent = fields.CharEnumField(model_enums.ContinentEnum)
    war_policy = fields.CharEnumField(model_enums.WarPolicyEnum)
    domestic_policy = fields.CharEnumField(model_enums.DomesticPolicyEnum)
    color: fields.ForeignKeyRelation["ColorModel"] = fields.ForeignKeyField(
        "pnwapi.ColorModel", related_name="nations")
    num_cities = fields.IntField()  # Is this needed?
    score = fields.FloatField()
    update_timezone = fields.IntField(default=0)
    population = fields.IntField()
    flag = fields.TextField()
    last_active = fields.DatetimeField()
    date_created = fields.DatetimeField()
    vacation_mode_turns = fields.IntField()
    beige_turns = fields.IntField()
    espionage_available = fields.BooleanField()
    turns_since_last_city = fields.IntField()
    turns_since_last_project = fields.IntField()
    project_bits = fields.IntField()

    # Military
    soldiers = fields.IntField()
    tanks = fields.IntField()
    aircraft = fields.IntField()
    ships = fields.IntField()
    missiles = fields.IntField()
    nukes = fields.IntField()
    spies = fields.IntField()

    # Stockpile
    money = fields.FloatField()
    coal = fields.FloatField()
    oil = fields.FloatField()
    uranium = fields.FloatField()
    iron = fields.FloatField()
    bauxite = fields.FloatField()
    lead = fields.FloatField()
    gasoline = fields.FloatField()
    munitions = fields.FloatField()
    steel = fields.FloatField()
    aluminum = fields.FloatField()
    food = fields.FloatField()

    # Statistics
    wars_won = fields.IntField()
    wars_lost = fields.IntField()
    alliance_seniority = fields.IntField()
    gross_national_income = fields.FloatField()
    gross_domectic_product = fields.FloatField()
    soldier_casualties = fields.IntField()
    soldier_kills = fields.IntField()
    tank_casualties = fields.IntField()
    tank_kills = fields.IntField()
    aircraft_casualties = fields.IntField()
    aircraft_kills = fields.IntField()
    ship_casualties = fields.IntField()
    ship_kills = fields.IntField()
    missile_casualties = fields.IntField()
    missile_kills = fields.IntField()
    nuke_casualties = fields.IntField()
    nuke_kills = fields.IntField()
    spy_casualties = fields.IntField()
    spy_kills = fields.IntField()
    spy_attacks = fields.IntField()
    money_looted = fields.FloatField()
    vip = fields.BooleanField()
    treasures: fields.ReverseRelation["TreasureModel"]

    alliance: fields.ForeignKeyRelation["AllianceModel"] = fields.ForeignKeyField(
        "pnwapi.AllianceModel", related_name="nations", null=True, on_delete=fields.SET_NULL, default=None)
    alliance_position: fields.ForeignKeyRelation["AlliancePositionModel"] = fields.ForeignKeyField(
        "pnwapi.AlliancePositionModel", related_name="nations", null=True, on_delete=fields.SET_NULL, default=None)
    tax_bracket: fields.ForeignKeyRelation["TaxBracketModel"] = fields.ForeignKeyField(
        "pnwapi.TaxBracketModel", related_name="nations", null=True, on_delete=fields.SET_NULL, default=None)
    tax_records: fields.ReverseRelation["TaxRecordModel"]

    cities: fields.ReverseRelation["CityModel"]
    offensive_wars: fields.ReverseRelation["WarModel"]
    defensive_wars: fields.ReverseRelation["WarModel"]

    _bank_records_sender: fields.ReverseRelation["BankRecordModel"]
    _bank_records_receiver: fields.ReverseRelation["BankRecordModel"]

    @property
    def bank_records(self) -> QuerySet["BankRecordModel"]:
        """Get all bank records for this nation. This is a property, not a field.

        Returns:
            All bank records for this nation.
        """
        # TODO: check which of these work, and or if there is a better way. Use the one that works the fastest.
        # self._bank_records_sender.remote_model.filter(
        #     expressions.Q(sender=self) | expressions.Q(receiver=self))
        return self._bank_records_sender.all() + self._bank_records_receiver.all()

    @property
    def wars(self) -> QuerySet["WarModel"]:
        """Get all wars this nation is involved in. This is a property, not a field.

        Returns:
            All wars this nation is involved in.
        """
        return self.offensive_wars.all() + self.defensive_wars.all()

    def __str__(self):
        return self.name

# async def dada():
#     nation = NationModel()

#     async for bankrecs in nation.bank_records.order_by("date"):
#         print(bankrecs)
