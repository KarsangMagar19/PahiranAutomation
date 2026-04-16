from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@class,'oxd-input') and @name='username']"))).send_keys("Admin")
driver.find_element(By.XPATH, "//input[contains(@class,'oxd-input') and @name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
wait.until(EC.url_contains("dashboard"))
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
actual_url=driver.current_url
if expected_url == actual_url:
    print("Test case PASSED")
else:
    print("Test case FAILED")

driver.quit()