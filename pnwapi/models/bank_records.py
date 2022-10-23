import typing

from tortoise.models import Model
from tortoise import fields
from . import model_enums

if typing.TYPE_CHECKING:
    from . import AllianceModel, NationModel


class BankRecordModel(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    sender_type = fields.IntEnumField(model_enums.BankRecordSenderTypeEnum)
    receiver_type = fields.IntEnumField(model_enums.BankRecordSenderTypeEnum)
    sender_nation: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="_bank_records_sender", on_delete=fields.SET_NULL, null=True)
    receiver_nation: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="_bank_records_reciever", on_delete=fields.SET_NULL, null=True)
    sender_alliance: fields.ForeignKeyRelation["AllianceModel"] = fields.ForeignKeyField(
        "pnwapi.AllianceModel", related_name="_bank_records_sender", on_delete=fields.SET_NULL, null=True)
    reciever_alliance: fields.ForeignKeyRelation["AllianceModel"] = fields.ForeignKeyField(
        "pnwapi.AllianceModel", related_name="_bank_records_reciever", on_delete=fields.SET_NULL, null=True)
    banker: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name=None, on_delete=fields.SET_NULL, null=True)

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

    def __str__(self):
        return self.id


class TaxRecordModel(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    nation: fields.ForeignKeyRelation["NationModel"] = fields.ForeignKeyField(
        "pnwapi.NationModel", related_name="tax_records", on_delete=fields.SET_NULL, null=True)
    alliance: fields.ForeignKeyRelation["AllianceModel"] = fields.ForeignKeyField(
        "pnwapi.AllianceModel", related_name="tax_records", on_delete=fields.SET_NULL, null=True)
    tax_id = fields.IntField()

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

    def __str__(self):
        return self.id
