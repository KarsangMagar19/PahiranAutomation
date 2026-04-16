from core.waits import Waits

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.waits = Waits(driver)

    def find(self, locator):
        return self.waits.wait_for_element(locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)