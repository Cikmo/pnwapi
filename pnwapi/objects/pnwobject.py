from abc import ABC, abstractmethod
from typing import TypeVar, Generic

PNWOBJECT = TypeVar("PNWOBJECT", bound="PnwObject")


class PnwObject():
    """Base class for all PnwObjects."""
    __slots__ = ()
