import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import ColorModel, NationModel


class TreasureModel(Model):
    name = fields.CharField(pk=True, max_length=50)
    color: fields.ForeignKeyRelation["ColorModel"] = fields.ForeignKeyField(
        "pnwapi.ColorModel", related_name=None)
    continent = fields.CharEnumField(model_enums.ContinentEnum)
    bonus = fields.IntField()
    spawn_date = fields.DatetimeField()
    nation: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="treasures", on_delete=fields.SET_NULL, null=True)

    def __str__(self):
        return self.name
