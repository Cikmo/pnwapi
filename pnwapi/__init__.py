import importlib.metadata as __importlib_metadata

__version__ = __importlib_metadata.version(__package__ or __name__)
del __importlib_metadata

from . import pnwapi as __pnwapi
from . import objects as __objects

__all__ = ("init", "nations", "alliances", "close_connections")

init = __pnwapi.Pnwapi.init

nations = __pnwapi.Interface(__objects.Nation)
alliances = __pnwapi.Interface(__objects.Alliance)


async def close_connections():
    """Cleanly close the aiohttp session and the database connections. This should be called when the program is exiting."""
    if __pnwapi.Pnwapi.api.aiohttp_session is not None:
        if (
            __pnwapi.Pnwapi.api.socket is not None
            and __pnwapi.Pnwapi.api.socket.task is not None
        ):
            __pnwapi.Pnwapi.api.socket.task.cancel()
        await __pnwapi.Pnwapi.api.aiohttp_session.close()
    if __pnwapi.Tortoise._inited:  # pyright: reportPrivateUsage=false
        await __pnwapi.Tortoise.close_connections()
