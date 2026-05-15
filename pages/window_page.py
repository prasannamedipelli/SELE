from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WindowPage:
    OPEN_NEW_WINDOW = (By.ID,"newWindowBtn")
    def __init__(self,driver):
        self.driver=driver
        
    def click_open_new_window(self):
        wait = WebDriverWait(self.driver,10)
        
        button = wait.until(EC.element_to_be_clickable(self.OPEN_NEW_WINDOW))
        button.click()
        
    
    def switch_to_child_window(self):
        #store ref to parent window
        parent_window = self.driver.current_window_handle
        
        WebDriverWait(self.driver,10).until(
            lambda d: len(d.window_handles) >1
        )
        all_window = self.driver.window_handles
        
        for window in all_window:
            if window != parent_window:
                self.driver.switch_to.window(window)
                break
            return parent_window
    def get_page_title(self):
        return self.driver.title
    
    def switch_back_to_parent_window(self, parent_window):
        self.driver.switch_to.window(parent_window) 