import importlib.metadata as _importlib_metadata

__version__ = _importlib_metadata.version(__package__ or __name__)

from .pnwapi import init
