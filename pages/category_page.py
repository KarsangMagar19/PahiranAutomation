from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CategoryPage(BasePage):
    # Locators
    ADD_CATEGORY_BUTTON = (By.XPATH, "//a[contains(., 'Add Category')] | //button[contains(., 'Add Category')]")
    CATEGORY_NAME_INPUT = (By.XPATH, "//input[@placeholder='e.g., Electronics, Clothing, Books']")
    CATEGORY_DESC_INPUT = (By.XPATH, "//textarea[@placeholder='Brief description of this category...']")
    CREATE_CATEGORY_BUTTON = (By.XPATH, "//button[normalize-space()='Create Category']")

    def click_add_category(self):
        self.click(self.ADD_CATEGORY_BUTTON)

    def fill_category_details(self, name, description):
        self.type(self.CATEGORY_NAME_INPUT, name)
        self.type(self.CATEGORY_DESC_INPUT, description)
        
    def submit_category(self):
        self.click(self.CREATE_CATEGORY_BUTTON)
