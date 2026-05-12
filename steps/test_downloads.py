from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios("../features/download.feature")


@given("user launches browser")
def launch_browser(driver):

    driver.get("https://the-internet.herokuapp.com/download")


@when("user switches to selenium iframe")
def switch_iframe(driver):

    pass


@when("user clicks Downloads link")
def click_download(driver):

    file_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='example']//a"
            )
        )
    )

    file_link.click()


@then("Downloads page should open")
def verify(driver):

    assert "download" in driver.current_url.lower()