import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

username = os.getenv("NAUKRI_USERNAME")
password = os.getenv("NAUKRI_PASSWORD")
resume_path = sys.argv[1]  # Resume.pdf path from CLI

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

driver.get('https://www.naukri.com/mnjuser/profile')

# Log in
driver.find_element(By.ID, 'usernameField').send_keys(username)
driver.find_element(By.ID, 'passwordField').send_keys(password)
driver.find_element(By.CLASS_NAME, 'loginBtn').click()

time.sleep(5)

# Navigate to resume upload
driver.get('https://www.naukri.com/mnjuser/profile/edit')

# Upload resume
upload_button = driver.find_element(By.XPATH, '//input[@type="file" and @name="resumeUpload"]')
upload_button.send_keys(os.path.abspath(resume_path))

time.sleep(10)  # wait for upload to complete

driver.quit()
