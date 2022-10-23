import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import NationModel, ColorModel, TreatyModel


class AllianceModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    acronym = fields.TextField()
    score = fields.FloatField()
    color: fields.ForeignKeyRelation["ColorModel"] = fields.ForeignKeyField(
        "pnwapi.ColorModel", related_name="alliances")
    average_score = fields.FloatField()
    treaties: fields.ReverseRelation["TreatyModel"]

    # alliance_positions: fields.ManyToManyRelation["AlliancePositionModel"] = fields.ManyToManyField(
    #     "pnwapi.AlliancePositionModel")

    #offensive_wars: fields.ReverseRelation["WarModel"]
    #defensive_wars: fields.ReverseRelation["WarModel"]
    nations: fields.ReverseRelation["NationModel"]

    def __str__(self):
        return self.name


# class AlliancePositionModel(Model):
#     id = fields.IntField(pk=True)
#     name = fields.TextField()

#     nations: fields.ReverseRelation["NationModel"]

#     def __str__(self):
#         return self.name


# class TaxBracketModel(Model):
#     id = fields.IntField(pk=True)
#     name = fields.TextField()
#     date_created = fields.DatetimeField()
#     date_modified = fields.DatetimeField()
#     last_modifier_id = fields.IntField()
#     tax_rate = fields.IntField()
#     resource_tax_rate = fields.IntField()

#     nations: fields.ReverseRelation["NationModel"]

#     def __str__(self):
#         return self.name
