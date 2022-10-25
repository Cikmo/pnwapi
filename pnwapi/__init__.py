import importlib.metadata as _importlib_metadata
from .pnwapi import Pnwapi
from .query import PnwQuerySet
from . import objects

__version__ = _importlib_metadata.version(__package__ or __name__)

init = Pnwapi.init

nations = PnwQuerySet(objects.Nation)
alliances = PnwQuerySet(objects.Alliance)
