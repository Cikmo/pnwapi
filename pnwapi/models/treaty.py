import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import AllianceModel


class TreatyModel(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    treaty_type = fields.CharEnumField(model_enums.TreatyTypeEnum)
    treaty_url = fields.TextField()
    turns_left = fields.IntField()
    alliances: fields.ManyToManyRelation["AllianceModel"] = fields.ManyToManyField(
        "pnwapi.AllianceModel", related_name="treaties")

    def __str__(self):
        return self.id
