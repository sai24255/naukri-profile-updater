from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Your Naukri credentials
email = "saicsk222@gmail.com"
password = "Saichukka@123"

# Start Chrome with more options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=options)

try:
    # Open Naukri login page
    print("Opening Naukri login page...")
    driver.get("https://www.naukri.com/nlogin/login")
    
    # Wait for any potential popups and close them
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class*='modal-close']"))).click()
        print("Closed popup if present")
    except TimeoutException:
        pass
    
    # Try multiple possible selectors for email field
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
    
    # Fill in the login form
    email_field.send_keys(email)
    print("Entered email")
    
    password_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Password']")
    password_field.send_keys(password)
    print("Entered password")
    
    # Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Clicked login button")
    
    # Wait for login to complete
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='dashboard']"))
        )
        print("Login successful!")
    except TimeoutException:
        print("Login verification failed - may still have logged in")
    
    # Add your profile update logic here
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
    # Take screenshot for debugging
    driver.save_screenshot("error.png")
    print("Screenshot saved as error.png")
    
finally:
    # Close the browser
    driver.quit()
    print("Browser closed")
