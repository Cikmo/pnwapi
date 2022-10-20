import logging
import pytest

log = logging.getLogger(__package__)


@pytest.fixture
def logger():
    return log
