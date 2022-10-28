from typing import TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from pnwkit.new import SubscriptionModelLiteral

PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject")


class PnwObject:
    """Base class for all PnwObjects."""

    __slots__ = ()
    _api_name: "SubscriptionModelLiteral"
