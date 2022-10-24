import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import NationModel


class BountyModel(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    nation: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="bounties", on_delete=fields.CASCADE)
    amount = fields.IntField()
    bounty_type = fields.CharEnumField(model_enums.BountyTypeEnum)

    def __str__(self):
        return self.id
