import pytest
from pages.seller_login_page import SellerLoginPage
from utils.data_reader import load_test_data

def test_successful_seller_login(driver):
    # Load test data
    test_data = load_test_data()
    seller_creds = test_data["seller_user"]
    
    # Initialize the page object
    login_page = SellerLoginPage(driver)
    
    # Navigate to the seller login page
    login_page.navigate_to()
    
    # Perform the login action
    login_page.login_as_seller(seller_creds["email"], seller_creds["password"])
    
    # Add assertions here after login
    # e.g., assert "Dashboard" in driver.title or check for a successful login element
