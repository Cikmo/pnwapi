import importlib.metadata as _importlib_metadata
from .pnwapi import Pnwapi

__version__ = _importlib_metadata.version(__package__ or __name__)
