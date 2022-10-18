from pnw import Pnw


def init(db_url: str,
         pnw_api_key: str,
         pnw_bot_key: str = None) -> Pnw:
    """
    Initialize pnwapi. This creates a singleton instance of the Pnw class, which can be accessed via the pnwapi.Pnw object.

    Args:
        db_url: The connection string for the database. See https://tortoise-orm.readthedocs.io/en/latest/databases.html#db-url for more information.
        pnw_api_key: The PnW API key to use for API requests.
        pnw_bot_key: The PnW bot key needed for certain PUT API requests. Defaults to None.

    Returns:
        A reference to the :class:`~pnwapi.pnw.Pnw` singleton instance.
    """
    pass
