import importlib.metadata as _importlib_metadata
from .pnwapi import Pnwapi
from .actions import Fetch

__version__ = _importlib_metadata.version(__package__ or __name__)

init = Pnwapi.init
fetch = Fetch
