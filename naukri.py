# naukri_update.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Fetch credentials and resume path from environment variables
USERNAME = os.environ['NAUKRI_USERNAME']
PASSWORD = os.environ['NAUKRI_PASSWORD']
RESUME_FILE = os.environ['RESUME_FILE']  # Full path to resume file

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.naukri.com/mnjuser/homepage")
    time.sleep(5)

    # Click Login
    login_button = driver.find_element(By.LINK_TEXT, "Login")
    login_button.click()
    time.sleep(3)

    # Enter credentials
    driver.find_element(By.NAME, "usernameField").send_keys(USERNAME)
    driver.find_element(By.NAME, "passwordField").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(8)

    print("Logged in successfully.")

    # Find the Resume Upload button
    upload_resume_button = driver.find_element(By.XPATH, "//input[@type='file' and contains(@name, 'resumeUpload')]")
    
    # Upload the resume
    upload_resume_button.send_keys(RESUME_FILE)
    print("Resume uploaded successfully.")

    # Wait for upload to finish
    time.sleep(10)

finally:
    driver.quit()
