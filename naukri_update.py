from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Your Naukri credentials
email = "saicsk222@gmail.com"
password = "Saichukka@123"

# Start Chrome in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# Open Naukri login page
driver.get("https://www.naukri.com/nlogin/login")

# Wait until Email field is present
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter Email ID / Username']")))

# Fill in the login form
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Email ID / Username']").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Password']").send_keys(password)

# Click Login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for few seconds to ensure login is complete
time.sleep(5)

# Close the browser
driver.quit()

