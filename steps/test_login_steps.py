#code behind file
from pytest_bdd import scenarios, given, when, then, parsers
import time
from pages.login_page import LoginPage
from openpyxl import load_workbook
from utils.db_utils import get_login_data
import pytest


#)
scenarios("../features/login.feature")

username, password = get_login_data() 
@given("user launches saucedemo site")
def launch_site(driver):
    page = LoginPage(driver)
    page.open()

@when(parsers.parse('user enters username'))
def enter_username(driver):
    page = LoginPage(driver)
    wb = load_workbook(r"C:\Users\shaik\Downloads\sele\sample.xlsx")
    page.enter_username(username)
    
@when(parsers.parse('user enters password'))
def enter_password(driver):
   
    page= LoginPage(driver)
    page.enter_password(password)
   

@when("user clicks login button")
def click_login(driver):
    page= LoginPage(driver)
    time.sleep(30)
    page.click_login()
  
    
@then("user should see products page")
def verify_pdoducts_page(driver):
    page= LoginPage(driver)
    assert "inventory" in driver.current_url
    

        
    
           
