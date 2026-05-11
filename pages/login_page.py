from selenium.webdriver.common.by import By

class LoginPage:
    username = (By.ID,"user-name")
    passwrod = (By.ID,"password")
    login_btn = (By.ID,"login-button")
  
    
    def __init__(self,driver):
        self.driver= driver
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
    
    def enter_username(self, user):
        self.driver.find_element(*self.username).send_keys(user)
        
    def enter_password(self, password):
        self.driver.find_element(*self.passwrod).send_keys(password)
      
    def click_login(self):
        self.driver.find_element(*self.login_btn).click()  
        
        
            