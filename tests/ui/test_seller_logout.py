import pytest
from pages.seller_login_page import SellerLoginPage
from pages.dashboard_page import DashboardPage
from utils.data_reader import load_test_data

def test_successful_seller_logout(driver):
    # Load test data
    test_data = load_test_data()
    seller_creds = test_data["seller_user"]
    
    # Initialize the page objects
    login_page = SellerLoginPage(driver)
    dashboard_page = DashboardPage(driver)
    
    # Navigate to the seller login page
    login_page.navigate_to()
    
    # Perform the login action
    login_page.login_as_seller(seller_creds["email"], seller_creds["password"])
    
    # Perform the logout action
    dashboard_page.logout()
