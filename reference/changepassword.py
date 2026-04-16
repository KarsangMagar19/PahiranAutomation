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
wait.until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class,'oxd-userdropdown-icon')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Change Password']"))).click()
wait.until(EC.url_contains("updatePassword"))
password_fields = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='password']")))
password_fields[0].send_keys("admin123")   # Current password
password_fields[1].send_keys("admin1234")  # New password
password_fields[2].send_keys("admin1234")  # Confirm password
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
wait.until(EC.url_contains("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"))
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
actual_url = driver.current_url
if expected_url in actual_url:
    print(" Test Case PASSED")
else:
    print(" Test Case FAILED")

driver.quit()