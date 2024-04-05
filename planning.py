import time
# from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.alert import Alert
# download_directory = 'C:\\Users\\Softech\\Pictures'
# chrome_options = Options()
# chrome_options.add_experimental_option("prefs", {
#     "download.default_directory": download_directory,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "safebrowsing.enabled": True
# })
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(service=Service('C:\\Users\\Softech\\PycharmProjects\\chromedriver.exe'))

# Configure Chrome options to set the download directory


driver.get('https://soluplanningdemo.meropalika.com/')
driver.maximize_window()
time.sleep(3)
# Find an element using XPath
element = driver.find_element(By.XPATH, '//*[@id="Email"]')
element.send_keys('planning@gmail.com')

element = driver.find_element(By.XPATH, '//*[@id="Password"]')
element.send_keys('123456')
time.sleep(3)
element = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/form/div[3]/input')
element.click()
time.sleep(3)

# lmbis
element = driver.find_element(By.XPATH, '//*[@id="wrapper"]/aside/div/div/ul/li[7]/a/span[3]/i')
for _ in range(2): element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="collapse-menu5"]/li[2]')
element.click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="FiscalYear"]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="FiscalYear"]/option[2]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="wardNo"]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="wardNo"]/option[3]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="pageSizeManual"]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="pageSizeManual"]/option[2]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="submit"]')
element.click()
time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="btnExport"]')
element.click()
time.sleep(5)

element = driver.find_element(By.XPATH, '//*[@id="wardNo"]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="wardNo"]/option[6]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="pageSizeManual"]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="pageSizeManual"]/option[2]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="submit"]')
element.click()
time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="btnExport"]')
element.click()
time.sleep(5)
