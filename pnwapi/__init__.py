import importlib.metadata as _importlib_metadata

from . import pnwapi
from . import objects

__version__ = _importlib_metadata.version(__package__ or __name__)


init = pnwapi.Pnwapi.init

nations = pnwapi.Interface(objects.Nation)
alliances = pnwapi.Interface(objects.Alliance)


async def close_connections():
    """Cleanly close the aiohttp session and the database connections. This should be called when the program is exiting."""
    await pnwapi.Pnwapi._api.aiohttp_session.close()
    await pnwapi.Tortoise.close_connections()
