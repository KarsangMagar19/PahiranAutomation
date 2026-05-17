from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import core.config as config

class Waits:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, config.TIMEOUT)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))