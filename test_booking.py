from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_booking():
    # Setup the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:5500/index.html")  # or your hosted URL

    # Scroll to Services section
    services_section = driver.find_element(By.ID, "services")
    driver.execute_script("arguments[0].scrollIntoView();", services_section)
    time.sleep(1)

    # Locate the "Book Now" button for Therapeutic Exercises
    book_button = driver.find_element(By.XPATH, "//button[contains(text(),'Therapeutic Exercises')]")
    book_button.click()
    time.sleep(1)

    # Accept the booking alert
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert Text: {alert_text}")
    alert.accept()

    driver.quit()

if __name__ == "__main__":
    test_booking()
