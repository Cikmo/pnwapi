import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import NationModel


class WarModel(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    reason = fields.TextField()
    war_type = fields.CharEnumField(model_enums.WarTypeEnum)

    ground_control = fields.IntField()
    air_superiority = fields.IntField()
    naval_blockage = fields.IntField()

    winner_id = fields.IntField()
    attacks: fields.ReverseRelation["WarAttackModel"]
    turns_left = fields.IntField()
    attacker: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="offensive_wars", on_delete=fields.SET_NULL, null=True)
    defender: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="defensive_wars", on_delete=fields.SET_NULL, null=True)
    attacker_MAPs = fields.IntField()
    defender_MAPs = fields.IntField()
    attacker_resistance = fields.IntField()
    defender_resistance = fields.IntField()
    attacker_offered_peace = fields.BooleanField()
    defender_offered_peace = fields.BooleanField()
    attacker_fotrified = fields.IntField()
    defender_fotrified = fields.IntField()
    attacker_gas_used = fields.IntField()
    defender_gas_used = fields.IntField()
    attacker_munitions_used = fields.IntField()
    defender_munitions_used = fields.IntField()
    attacker_aluminum_used = fields.IntField()
    defender_aluminum_used = fields.IntField()
    attacker_steel_used = fields.IntField()
    defender_steel_used = fields.IntField()
    attacker_infra_destroyed = fields.IntField()
    defender_infra_destroyed = fields.IntField()
    attacker_money_looted = fields.FloatField()
    defender_money_looted = fields.FloatField()
    attacker_soldiers_killed = fields.IntField()
    defender_soldiers_killed = fields.IntField()
    attacker_tanks_killed = fields.IntField()
    defender_tanks_killed = fields.IntField()
    attacker_aircraft_killed = fields.IntField()
    defender_aircraft_killed = fields.IntField()
    attacker_ships_killed = fields.IntField()
    defender_ships_killed = fields.IntField()
    attacker_missiles_used = fields.IntField()
    defender_missiles_used = fields.IntField()
    attacker_nukes_used = fields.IntField()
    defender_nukes_used = fields.IntField()
    attacker_infra_destroyed_value = fields.IntField()
    defender_infra_destroyed_value = fields.IntField()

    def __str__(self):
        return self.id


class WarAttackModel(Model):
    id = fields.IntField(pk=True)
    war: fields.ForeignKeyRelation["WarModel"] = fields.ForeignKeyField(
        "pnwapi.WarModel", related_name="attacks", on_delete=fields.CASCADE)
    date = fields.DatetimeField()
    attacker = fields.IntField()
    defender = fields.IntField()
    attack_type = fields.CharEnumField(model_enums.WarAttackTypeEnum)
    victor = fields.IntField()
    success = fields.IntEnumField(model_enums.WarAttackOutcomeEnum)
    attacker_casualties1 = fields.IntField()
    attacker_casualties2 = fields.IntField()
    defender_casualties1 = fields.IntField()
    defender_casualties2 = fields.IntField()
    city_id = fields.IntField()
    infra_destroyed = fields.FloatField()
    improvements_lost = fields.IntField()
    money_stolen = fields.FloatField()
    loot_info = fields.TextField()
    resistance_eliminated = fields.IntField()
    city_infra_before = fields.IntField()
    infra_destroyed_value = fields.FloatField()
    attacker_munitions_used = fields.FloatField()
    attacker_gasoline_used = fields.FloatField
    defender_munitions_used = fields.FloatField()
    defender_gasoline_used = fields.FloatField()
    aircraft_killed_by_tanks = fields.IntField()

    def __str__(self):
        return self.id
