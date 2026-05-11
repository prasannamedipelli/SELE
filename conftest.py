import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")
    driver= webdriver.Chrome()
    
    yield driver
    driver.quit()