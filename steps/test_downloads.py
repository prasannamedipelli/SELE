from pytest_bdd import scenarios , given, when, then
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#)
scenarios(r"../features/download.feature")

@given("user launches browser")
def launch_browser(driver):
    
    #.maximize_window()
    driver.get("https://practice-automation.com/iframes/")


@when("user switches to selenium iframe")
def switch_iframe(driver):
    iframe = WebDriverWait(driver,10).until(
        EC.presence_of_element_located
        ((By.ID,"iframe-2"))
    )
    driver.switch_to.frame(iframe)
    
    # dynamic wait
    
@when("user clicks Downloads link")
def click_download(driver):
    downloads =  WebDriverWait(driver,20).until(
        EC.presence_of_all_elements_located((By.XPATH,"//a[contains(text(),'Downloads')]"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", downloads
    )
    
@then("Downloads page should open")
def verify(driver):
    assert "downloads" in driver.current_url.lower()
    
    
