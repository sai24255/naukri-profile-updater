from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

driver.get('https://www.naukri.com/nlogin/login')

time.sleep(2)

driver.find_element("id", "usernameField").send_keys(email)
driver.find_element("id", "passwordField").send_keys(password)
driver.find_element("xpath", "//button[@type='submit']").click()

time.sleep(5)

# ...your code here...

driver.quit()
