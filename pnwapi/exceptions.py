# exceptions.py

class PnwapiError(Exception):
    """
    Base class for all pnwapi exceptions.
    """
    pass


class NotInitializedError(PnwapiError):
    """
    Raised when a function is called before pnwapi has been initialized.
    """
    pass


class AlreadyInitializedError(PnwapiError):
    """
    Raised when pnwapi.init() is called more than once.
    """
    pass


class InvalidApiKeyError(PnwapiError):
    """
    Raised when an invalid API key is provided.
    """
    pass


class InvalidDatabaseUrl(PnwapiError):
    """
    Raised when an invalid database URL is provided.
    """
    pass


class DatabaseConnectionError(PnwapiError):
    """
    Raised when a database connection error occurs.
    """
    pass
