import time
from nepali_date_converter import DateConverter
from datetime import datetime
from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from nepali_date_converter import english_to_nepali_converter
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service('C:\\Users\\Softech\\PycharmProjects\\chromedriver.exe'))

# Navigate to a webpage
driver.maximize_window()
current_date = datetime.now().strftime("%Y-%m-%d")
driver.get('http://planningdemo.meropalika.com/Admin/Home')

time.sleep(3)
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
element = driver.find_element(By.XPATH, '//*[@id="YojanaEndDate"]')
element.send_keys(current_date)
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