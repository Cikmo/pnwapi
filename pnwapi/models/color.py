import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import NationModel, AllianceModel


class ColorModel(Model):
    color = fields.CharEnumField(model_enums.ColorEnum, pk=True)
    bloc_name = fields.TextField()
    turn_bonus = fields.IntField()

    nations = fields.ReverseRelation["NationModel"]
    alliances = fields.ReverseRelation["AllianceModel"]

    def __str__(self):
        return self.color
