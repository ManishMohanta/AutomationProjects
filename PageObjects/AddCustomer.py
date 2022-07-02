from selenium.webdriver.common.by import By


class AddCustomer:
    Email = "//input[@id='Email']"
    Password = "//input[@id='Password']"
    FirstName = "//input[@id='FirstName']"
    LastName = "//input[@id='FirstName']"
    Gender = "//input[@id='Gender_Male']"
    CompanyName = "//input[@id='Company']"
    IsTAxExempt = "//input[@id='Company']"
    NewsLetter = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    Active = "//input[@id='Active']"
    Admin_comment = "//textarea[@id='AdminComment']"
    Save = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def setemail(self, mail):
        self.driver.find_element(By.XPATH, self.Email).send_keys('xxx@yyy.com')
    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.Password).send_keys('xxx')
    def setfirstname(self,firstname):
        self.driver.find_element(By.XPATH, self.FirstName).send_keys('Mk')
    def setlastname(self, lastname):
        self.driver.find_element(By.XPATH, self.LastName).send_keys('Mk')
    def gender(self, gender):
        self.driver.find_element(By.XPATH, self.Gender).click()
    def setcompanyname(self,companyname):
        self.driver.find_element(By.XPATH,self.CompanyName).send_keys('Mk')
    def saveuser(self,save):
        self.driver.find_element(By.XPATH, self.Save).click()