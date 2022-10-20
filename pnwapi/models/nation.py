import typing
from . import model_enums

from tortoise.models import Model
from tortoise import fields

if typing.TYPE_CHECKING:
    ...


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
    color = fields.CharEnumField(model_enums.ColorEnum)
    num_cities = fields.IntField()  # Is this needed?
    score = fields.FloatField()
    update_timezone = fields.IntField(default=0)
    population = fields.IntField()
    flag_url = fields.TextField()
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

    # alliance: fields.ForeignKeyRelation["AllianceModel"] = fields.ForeignKeyField(
    #     "pnwdb.AllianceModel", related_name="nations", null=True, on_delete=fields.SET_NULL, default=None)
    # alliance_position: fields.ForeignKeyRelation["AlliancePositionModel"] = fields.ForeignKeyField(
    #     "pnwdb.AlliancePositionModel", related_name="nations", null=True, on_delete=fields.SET_NULL, default=None)
    # tax_bracket: fields.ForeignKeyRelation["TaxBracketModel"] = fields.ForeignKeyField(
    #     "pnwdb.TaxBracketModel", related_name="nations", null=True, on_delete=fields.SET_NULL, default=None)

    # cities: fields.ReverseRelation["CityModel"]
    # offensive_wars: fields.ReverseRelation["WarModel"]
    # defensive_wars: fields.ReverseRelation["WarModel"]
    #bounties: fields.ReverseRelation["Bounty"]

    # The following should be fetched direclty from API, instead of saving in db
    #   bank_records = fields.ManyToManyField("models.BankRecord")
    #   trades = fields.ManyToManyField("models.Trade", related_name="nations")
    #   treasures = fields.ManyToManyField("models.Treasure", related_name="nation")
    #   tax_records

    def __str__(self):
        return self.name
