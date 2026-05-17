from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Locators
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='submit']")
    CATEGORY_VIEW_BUTTON = (By.XPATH, "//a[contains(@href, 'categor') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'categor')]")

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def navigate_to_categories(self):
        import time
        time.sleep(2) # Wait for dashboard to fully load
        self.click(self.CATEGORY_VIEW_BUTTON)
