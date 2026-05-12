import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=option)
    # driver= webdriver.Chrome()  # webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub" , options=option
        
    # )
    
    
    yield driver
    driver.quit()