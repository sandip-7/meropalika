import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from nepali_date_converter import english_to_nepali_converter
from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import Select
# Initialize the WebDriver
# def convert_to_nepali(english_date):
#     # For demonstration, let's assume we're just adding 57 years to the English year
#     # english_year = int(english_date[0])
#     # nepali_year = english_year + 57
#     english_year = int(current_date.split("-")[0])
#     english_month = int(current_date.split("-")[1])
#     english_day = int(current_date.split("-")[2])
#     nepali_year = english_year + 57
#     nepali_date = f"{nepali_year:04d}-{english_month:02d}-{english_day:02d}"
#
#     # Constructing a simple Nepali date format
#     # nepali_date = f"{nepali_year}-01-01"  # Assuming first day of the year
#
#     return nepali_date

def convert_to_nepali(english_date):
    # For demonstration, let's assume we're just adding 57 years to the English year
    # english_year = int(english_date[0])
    # nepali_year = english_year + 57
    english_year = int(current_date.split("-")[0])
    english_month = int(current_date.split("-")[1])
    english_day = int(current_date.split("-")[2])
    nepali_year = english_year + 57
    nepali_date = f"{nepali_year:04d}-{english_month:02d}-{english_day:02d}"

    # Constructing a simple Nepali date format
    # nepali_date = f"{nepali_year}-01-01"  # Assuming first day of the year

    return nepali_date


driver = webdriver.Chrome(service=Service('C:\\Users\\Softech\\PycharmProjects\\chromedriver.exe'))

# Navigate to a webpage
driver.maximize_window()
driver.get('http://planningdemo.meropalika.com/Admin/Home')

time.sleep(3)
# element = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[3]/div[1]/button')
# element.click()
# time.sleep(3)
# Find an element using XPath
element = driver.find_element(By.XPATH, '//*[@id="Email"]')
element.send_keys('planning@gmail.com')

element = driver.find_element(By.XPATH, '//*[@id="Password"]')
element.send_keys('123456')
time.sleep(3)
# login click
element = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div/div/div/form/div[3]/input')
element.click()
time.sleep(3)
# lmbis
element = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div/ul/li[4]')
element.click()
element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/aside/div/div/ul/li[4]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="sidebar"]/div/div/ul/li[4]/ul/li[1]/a/span[2]')
element.click()
time.sleep(3)
# ba u sse
element = driver.find_element(By.XPATH, '//*[@id="select2-BudgetUpasirshakId-container"]')
element.click()
time.sleep(3)

# dropdown = driver.find_element(By.XPATH, '//*[@id="select2-BudgetUpasirshakId-container"]')
# select = Select(dropdown)
# element = driver.find_element(By.XPATH, '//*[@id="select2-OfficeId-container"]')
# element.click()
# time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="BudgetUpasirshakId"]/option[2]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/form/div[3]/div/span['
                                        '1]/span[1]/span')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="OfficeId"]/option[2]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="YojanaStartDate"]')
element.send_keys('2079-12-01')
# element.click()
time.sleep(3)

# Get current English date
current_date = datetime.now().strftime("%Y-%m-%d")

# Convert current English date to Nepali date
nepali_date = convert_to_nepali(current_date)


element = driver.find_element(By.XPATH, '//*[@id="YojanaEndDate"]')
element.send_keys(nepali_date)
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/form/div[6]')
element.click()
time.sleep(3)
keyboard = Controller()
keyboard.type("C:\\Users\\Softech\\Downloads\\Payroll.xls")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="Submit"]')
element.click()
time.sleep(3)
# next
# ba u se n
element = driver.find_element(By.XPATH, '//*[@id="select2-BudgetUpasirshakId-container"]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="BudgetUpasirshakId"]/option[2]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/form/div[3]/div/span['
                                        '1]/span[1]/span')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="OfficeId"]/option[3]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="YojanaStartDate"]')
element.send_keys('2079-12-01')
# element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="YojanaEndDate"]')
element.send_keys('2080-12-01')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/form/div[6]')
element.click()
time.sleep(3)
keyboard = Controller()
keyboard.type("C:\\Users\\Softech\\Downloads\\Payroll.xls")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="Submit"]')
element.click()
time.sleep(3)
# next
# ba u se n
element = driver.find_element(By.XPATH, '//*[@id="select2-BudgetUpasirshakId-container"]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="BudgetUpasirshakId"]/option[2]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/form/div[3]/div/span['
                                        '1]/span[1]/span')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="OfficeId"]/option[4]')
element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="YojanaStartDate"]')
element.send_keys('2079-12-01')
# element.click()

time.sleep(3)


element.click()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div/div/div/div[1]/form/div[6]')
element.click()
time.sleep(3)
