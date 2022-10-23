import typing

from tortoise.models import Model
from tortoise import fields

if typing.TYPE_CHECKING:
    from . import NationModel


class CityModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    date_created = fields.DatetimeField()
    infrastructure = fields.FloatField()
    land = fields.FloatField()
    powered = fields.BooleanField()
    oil_power = fields.IntField()
    wind_power = fields.IntField()
    coal_power = fields.IntField()
    nuclear_power = fields.IntField()
    coal_mine = fields.IntField()
    oil_well = fields.IntField()
    uranium_mine = fields.IntField()
    barracks = fields.IntField()
    farm = fields.IntField()
    police_station = fields.IntField()
    hospital = fields.IntField()
    recycling_center = fields.IntField()
    subway = fields.IntField()
    supermarket = fields.IntField()
    bank = fields.IntField()
    shopping_mall = fields.IntField()
    stadium = fields.IntField()
    lead_mine = fields.IntField()
    iron_mine = fields.IntField()
    bauxite_mine = fields.IntField()
    oil_refinery = fields.IntField()
    aluminum_refinery = fields.IntField()
    steel_mill = fields.IntField()
    munitions_factory = fields.IntField()
    factory = fields.IntField()
    hangar = fields.IntField()
    drydock = fields.IntField()
    nuke_date = fields.DatetimeField(null=True, default=None)

    nation: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="cities")

    def __str__(self):
        return self.name
