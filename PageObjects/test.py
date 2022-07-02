from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')

driver.get('https://admin-demo.nopcommerce.com/login')

driver.find_element(By.XPATH, "//button[@type='submit']").click()