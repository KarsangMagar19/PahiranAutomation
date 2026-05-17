import pytest
from core.driver_factory import get_driver
import core.config as config

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get(config.BASE_URL)
    yield driver
    driver.quit()