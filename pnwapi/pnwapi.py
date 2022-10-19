import asyncio
import os
import pnwkit
import sys
import logging

from tortoise import Tortoise

logger = logging.getLogger(__name__)


class Pnwapi:
    def __init__(self):
        self._PNW_API_KEY: str

        self._api: pnwkit.QueryKit

    @classmethod
    async def init(cls, db_url: str,
                   pnw_api_key: str,
                   pnw_bot_key: str = None) -> "Pnwapi":
        """
        Initialize pnwapi. This creates a singleton instance of the Pnw class, which can be accessed via the pnwapi.Pnw object.

        Args:
            db_url: The connection string for the database. See https://tortoise-orm.readthedocs.io/en/latest/databases.html#db-url for more information.
            pnw_api_key: The PnW API key to use for API requests.
            pnw_bot_key: The PnW bot key needed for certain PUT API requests. Defaults to None.

        Returns:
            A reference to the :class:`~pnwapi.pnw.Pnw` singleton instance.
        """
        pnwapi = cls()
        pnwapi._PNW_API_KEY = pnw_api_key

        pnwapi._api = pnwkit.QueryKit(pnw_api_key, pnw_bot_key)

        # Only initialize the DB if we're not in a test environment.
        # Tests use a seperate initializer found in the `tests/fixtures.py` file.
        if not "pytest" in sys.modules:
            logger.warning(
                "If this is a test, you shouldn't see this message. You can safely ignore this warning if this is not a test. This warning is located in pnwapi.py in the Pnwapi.init() function.")
            tortoise_config = {
                'connections': {
                    'default': db_url
                },
                'apps': {
                    'pnwdb': {
                        'models': ['pnwdb.models'],
                        'default_connection': 'default',
                    }
                },
                'use_tz': False,
                'timezone': 'UTC'
            }

            # await Tortoise.init(config=tortoise_config)
            # await Tortoise.generate_schemas()

        return pnwapi


async def test():
    await Pnwapi.init("sqlite://:memory:", "1241521525", "1221531527")

asyncio.run(test())
