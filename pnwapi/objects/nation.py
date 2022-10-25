from .pnwobject import PnwObject
from . import alliance


class Nation(PnwObject):
    __slots__ = ("id", "name", "alliance")

    def __init__(self):
        self.id: int
        self.name: str
        self.alliance: alliance
