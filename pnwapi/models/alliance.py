import typing

from tortoise.models import Model
from tortoise import fields
from tortoise.queryset import QuerySet
from . import model_enums

if typing.TYPE_CHECKING:
    from . import (NationModel,
                   ColorModel,
                   TreatyModel,
                   BankRecordModel,
                   TaxRecordModel,
                   WarModel)


class AllianceModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    acronym = fields.TextField()
    score = fields.FloatField()
    color: fields.ForeignKeyRelation["ColorModel"] = fields.ForeignKeyField(
        "pnwapi.ColorModel", related_name="alliances")
    average_score = fields.FloatField()
    treaties: fields.ReverseRelation["TreatyModel"]
    alliance_positions: fields.ReverseRelation["AlliancePositionModel"]
    accept_members = fields.BooleanField()
    flag = fields.TextField()
    forum_link = fields.TextField()
    discord_link = fields.TextField()
    wiki_link = fields.TextField()
    tax_brackets: fields.ReverseRelation["TaxBracketModel"]
    tax_records: fields.ReverseRelation["TaxRecordModel"]

    nations: fields.ReverseRelation["NationModel"]

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

    _bank_records_sender: fields.ReverseRelation["BankRecordModel"]
    _bank_records_receiver: fields.ReverseRelation["BankRecordModel"]

    @property
    def bank_records(self) -> QuerySet["BankRecordModel"]:
        """Get all bank records for this alliance. This is a property, not a field.

        Returns:
            All bank records for this nation.
        """
        # TODO: check which of these work, and or if there is a better way. Use the one that works the fastest.
        # self._bank_records_sender.remote_model.filter(
        #     expressions.Q(sender=self) | expressions.Q(receiver=self))
        return self._bank_records_sender.all() + self._bank_records_receiver.all()

    def __str__(self):
        return self.name


class AlliancePositionModel(Model):
    id = fields.IntField(pk=True)
    date_created = fields.DatetimeField()
    alliance: fields.ForeignKeyRelation["AllianceModel"] = fields.ForeignKeyField(
        "pnwapi.AllianceModel", related_name="alliance_positions")
    name = fields.TextField()
    creator_id = fields.IntField()
    last_editor_id = fields.IntField()
    date_modified = fields.DatetimeField()
    position_level = fields.IntField()

    leader = fields.BooleanField()
    heir = fields.BooleanField()
    officer = fields.BooleanField()
    member = fields.BooleanField()

    permissions = fields.IntField()

    view_bank = fields.BooleanField()
    withdraw_bank = fields.BooleanField()
    change_permissions = fields.BooleanField()
    see_spies = fields.BooleanField()
    see_reset_timer = fields.BooleanField()
    tax_brackets = fields.BooleanField()
    post_announcements = fields.BooleanField()
    accept_applicants = fields.BooleanField()
    remove_members = fields.BooleanField()
    edit_alliance_info = fields.BooleanField()
    manage_treaties = fields.BooleanField()
    manage_market_share = fields.BooleanField()
    manage_embargoes = fields.BooleanField()
    promote_self_to_leader = fields.BooleanField()

    nations: fields.ReverseRelation["NationModel"]

    def __str__(self):
        return self.name


class TaxBracketModel(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    date_created = fields.DatetimeField()
    date_modified = fields.DatetimeField()
    last_modifier_id = fields.IntField()
    tax_rate = fields.IntField()
    resource_tax_rate = fields.IntField()
    alliance: fields.ForeignKeyRelation["AllianceModel"] = fields.ForeignKeyField(
        "pnwapi.AllianceModel", related_name="tax_brackets", on_delete=fields.CASCADE)
    nations: fields.ReverseRelation["NationModel"]

    def __str__(self):
        return self.name
