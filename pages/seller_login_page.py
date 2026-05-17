import core.config as config
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SellerLoginPage(BasePage):
    URL = config.BASE_URL
    
    # Locators
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login as Seller']")
    
    def navigate_to(self):
        self.driver.get(self.URL)

    def login_as_seller(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
