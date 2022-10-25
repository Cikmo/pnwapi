from .pnwobject import PnwObject
from . import nation


class Alliance(PnwObject):
    __slots__ = ("id", "name")

    def __init__(self):
        self.id: int
        self.name: str
