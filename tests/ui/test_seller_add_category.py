import pytest
from pages.seller_login_page import SellerLoginPage
from pages.dashboard_page import DashboardPage
from pages.category_page import CategoryPage
from utils.data_reader import load_test_data

def test_seller_add_category(driver):
    # Load test data
    test_data = load_test_data()
    seller_creds = test_data["seller_user"]
    
    # Initialize the page objects
    login_page = SellerLoginPage(driver)
    dashboard_page = DashboardPage(driver)
    category_page = CategoryPage(driver)
    
    # Navigate to the seller login page
    login_page.navigate_to()
    
    # Perform the login action
    login_page.login_as_seller(seller_creds["email"], seller_creds["password"])
    
    # Click on the category view button
    dashboard_page.navigate_to_categories()
    
    # Click on add category
    category_page.click_add_category()
    
    # Fill in category details
    category_page.fill_category_details("cate1", "hello")
    
    # Submit the category
    category_page.submit_category()
