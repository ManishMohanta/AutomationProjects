import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from PageObjects.LoginPage import LoginPage

class Test_01_Addcustomer():

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    def test_adduser(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.loginbutton()
        # self.driver.find_element(By.XPATH, "//body/div[3]/nav[1]/ul[1]/li[1]/a[1]/i[1]").click()
        self.driver.find_element(By.XPATH, "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]").click()
        self.driver.find_element(By.XPATH, "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]").click()

        self.au = AddCustomer(self.driver)
        self.au.setemail(self)
        self.au.setpassword(self)

