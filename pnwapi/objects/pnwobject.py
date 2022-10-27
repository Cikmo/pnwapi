from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from .. import pnwapi

PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject")


class PnwObject:
    """Base class for all PnwObjects."""
    #__slots__ = ()
    _api_name: str
