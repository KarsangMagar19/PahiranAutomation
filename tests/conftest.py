import pytest
from core.driver_factory import get_driver
from core.config import Config

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()