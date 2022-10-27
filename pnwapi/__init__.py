import importlib.metadata as __importlib_metadata  # nopep8
__version__ = __importlib_metadata.version(__package__ or __name__)  # nopep8
del __importlib_metadata  # nopep8

from . import pnwapi as __pnwapi
from . import objects as __objects

__all__ = ("init", "nations", "alliances", "close_connections")

init = __pnwapi.Pnwapi.init

nations = __pnwapi.Interface(__objects.Nation)
alliances = __pnwapi.Interface(__objects.Alliance)


async def close_connections():
    """Cleanly close the aiohttp session and the database connections. This should be called when the program is exiting."""
    await __pnwapi.Pnwapi._api.aiohttp_session.close()
    await __pnwapi.Tortoise.close_connections()
