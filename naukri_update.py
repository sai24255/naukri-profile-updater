from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import tempfile
import shutil
import os

# Your Naukri credentials
email = "saicsk222@gmail.com"
password = "Saichukka@123"

# Start Chrome with more options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Use visible mode for debugging by commenting this line
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Use unique temp directory to avoid profile conflict
user_data_dir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={user_data_dir}")

# Initialize Chrome driver
driver = webdriver.Chrome(options=options)

try:
    print("Opening Naukri login page...")
    driver.get("https://www.naukri.com/nlogin/login?URL=//www.naukri.com/mnjuser/profile")

    # Close popup if present
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[class*='modal-close']"))
        ).click()
        print("Closed popup if present")
    except TimeoutException:
        pass

    # Locate email input field
    email_selectors = [
        "input[placeholder='Enter Email ID / Username']",
        "input[placeholder='Enter your active Email ID / Username']",
        "input[id='usernameField']",
        "input[name='email']"
    ]

    email_field = None
    for selector in email_selectors:
        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            print(f"Found email field with selector: {selector}")
            break
        except TimeoutException:
            continue

    if not email_field:
        raise Exception("Could not find email field with any selector")

    email_field.send_keys(email)
    print("Entered email")

    password_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Password']")
    password_field.send_keys(password)
    print("Entered password")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Clicked login button")

    # Check for login success via URL or element
    login_success = False
    try:
        WebDriverWait(driver, 15).until(EC.url_contains("mnjuser/profile"))
        print("Login successful! Redirected to profile.")
        login_success = True
    except TimeoutException:
        print("URL did not change, checking fallback element...")

    if not login_success:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.nI-gNb-drawer"))
            )
            print("Login probably successful - profile menu found.")
            login_success = True
        except TimeoutException:
            print("Login verification failed - still on login page.")

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    screenshot_name = "post_login_success.png" if login_success else "post_login_fail.png"
    driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved as {screenshot_name}")

    # 👉 TODO: Add your profile update/resume upload logic here

except Exception as e:
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error.png")
    print("Screenshot saved as error.png")

finally:
    driver.quit()
    print("Browser closed")
    shutil.rmtree(user_data_dir)
    print("Temporary user data directory deleted")
