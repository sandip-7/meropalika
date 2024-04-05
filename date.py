import time

from selenium import webdriver
from datetime import datetime
import nepali_date_converter

# Initialize the WebDriver (assuming you've set it up properly)
driver = webdriver.Chrome()

# Get the current date in English
current_date = datetime.now().strftime("%Y-%m-%d")

# Convert English date to Nepali date
current_nepali_date = nepali_date_converter.english_to_nepali(current_date)

# Print the current Nepali date
print("Current Nepali Date:", current_nepali_date)

# Quit the WebDriver session
driver.quit()
time.sleep(5)
