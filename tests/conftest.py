import time

import pytest


@pytest.fixture(scope='function')
def throttle():
    yield
    time.sleep(.5)
