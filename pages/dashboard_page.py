from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Locators
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
