import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import ColorModel, NationModel


class TreasureModel(Model):
    name = fields.TextField(pk=True)
    color: fields.ForeignKeyRelation["ColorModel"] = fields.ForeignKeyField(
        "pnwapi.ColorModel", related_name=None)
    continent = fields.CharEnumField(model_enums.ContinentEnum)
    bonus = fields.IntField()
    spawn_date = fields.DatetimeField()
    nation: fields.OneToOneRelation["NationModel"] = fields.OneToOneField(
        "pnwapi.NationModel", related_name="treasure", on_delete=fields.SET_NULL)

    def __str__(self):
        return self.id
