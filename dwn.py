import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Specify the download directory
download_directory = 'C:\\Users\\Softech\\Pictures'

# Configure Chrome options to set the download directory
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open a webpage where the file download is initiated
driver.get("https://myjob.page/tools/test-files")

# Find the element that triggers the file download
element = driver.find_element(By.XPATH, '//*[@id="vue"]/div[1]/a[1]')
for _ in range(5): element.click()
time.sleep(7)
# Click the download link
driver.get("https://www.geeksforgeeks.org/navigating-links-using-get-method-selenium-python/?ref=lbp")
# Quit the WebDriver session after the download is complete
driver.quit()
