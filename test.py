import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service('C:\\Users\\Softech\\PycharmProjects\\chromedriver.exe'))
driver.get('https://demoqa.com/alerts')
driver.maximize_window()
time.sleep(3)
element = driver.find_element(By.XPATH, '//*[@id="alertButton"]')
element.click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()

time.sleep(5)
