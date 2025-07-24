from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tempfile
import os
import shutil

# === User Inputs ===
NAUKRI_EMAIL = "your_email@example.com"
NAUKRI_PASSWORD = "your_password"
RESUME_PATH = "/path/to/your_resume.pdf"  # PDF/DOC/RTF (max 2MB)

# === Chrome Setup ===
options = Options()
options.add_argument("--headless=new")  # Optional: run headless
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
user_data_dir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

try:
    # === 1. Open Naukri Login Page ===
    driver.get("https://www.naukri.com/nlogin/login?URL=//www.naukri.com/mnjuser/profile")
    print("Opened login page")

    # === 2. Fill Credentials ===
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter Email ID / Username']"))).send_keys(NAUKRI_EMAIL)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys(NAUKRI_PASSWORD)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    print("Logged in")

    # === 3. Go to Profile Page ===
    wait.until(EC.url_contains("profile"))
    print("Navigated to profile")

    # === 4. Wait for Resume Section ===
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Update resume']")))

    # === 5. Click 'Update resume' Button ===
    upload_button = driver.find_element(By.XPATH, "//button[text()='Update resume']")
    driver.execute_script("arguments[0].click();", upload_button)
    print("Clicked update button")

    # === 6. Upload File ===
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(RESUME_PATH)
    print("Resume uploaded successfully")

    time.sleep(5)  # Allow upload to complete

except Exception as e:
    print(f"❌ Error occurred: {e}")
finally:
    driver.quit()
    shutil.rmtree(user_data_dir)
