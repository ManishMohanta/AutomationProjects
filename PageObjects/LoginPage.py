from selenium.webdriver.common.by import By


class LoginPage:

    Email = "//input[@id='Email']"
    Password = "//input[@id='Password']"
    Lgnbutton = "//button[@type='submit']"


    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(
            By.XPATH, self.Email).clear()
        self.driver.find_element(By.XPATH, self.Email).send_keys('admin@yourstore.com')

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.Password).clear()
        self.driver.find_element(By.XPATH, self.Password).send_keys('admin')

    def loginbutton(self):
        self.driver.find_element(By.XPATH, self.Lgnbutton).click()

