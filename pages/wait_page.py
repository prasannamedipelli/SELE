from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class WaitsPage:
    ADD_TEXTBOX_BTN = (By.ID, "btn1")
    TEXTBOX1 = (By.ID, "txt1")
    def __init__(self,driver):
        self.driver = driver
        
    def click_add_textbox(self):
        self.driver.find_element(*self.ADD_TEXTBOX_BTN).click()
        
    def wait_for_text_box1(self):
            
        #create a wait object
        # wait = WebDriverWait(self.driver,100)
        
        # #create textbox and add wait to that 
        # textbox= wait.until(EC.visibility_of_element_located(self.TEXTBOX1))
        textbox = self.driver.find_element(*self.TEXTBOX1)
        return textbox.is_displayed()