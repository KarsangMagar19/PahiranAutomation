from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.config import Config

class Waits:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))