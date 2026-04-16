from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"))).click()
wait.until(EC.url_contains("requestPasswordResetCode"))
forgot_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
forgot_input.send_keys("Admin")
reset_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
reset_button.click()
wait.until(EC.url_contains("sendPasswordReset"))
print("Forgot Password flow executed successfully")

driver.quit()