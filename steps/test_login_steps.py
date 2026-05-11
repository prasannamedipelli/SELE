#code behind file
from pytest_bdd import scenarios, given, when, then, parsers
import time
from pages.login_page import LoginPage


scenarios("../features/login.feature")

@given("user launches saucedemo site")
def launch_site(driver):
    page = LoginPage(driver)
    page.open()

@when(parsers.parse('user enters username "{username}"'))
def enter_username(driver, username):
    page = LoginPage(driver)
   
    page.enter_username(username)
    
@when(parsers.parse('user enters password "{password}"'))
def enter_password(driver, password):
   
    page= LoginPage(driver)
    page.enter_password(password)
   

@when("user clicks login button")
def click_login(driver):
    page= LoginPage(driver)
    
    page.click_login()
    time.sleep(30)
    
@then("user should see products page")
def verify_pdoducts_page(driver):
    page= LoginPage(driver)
    assert "inventory" in driver.current_url
    

        
    
           