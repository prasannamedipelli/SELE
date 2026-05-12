from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Load all scenarios from feature file
scenarios("../features/login.feature")


# Launch Website
@given("user launches saucedemo site")
def launch_site(driver):

    page = LoginPage(driver)
    page.open()


# Enter Username
@when(parsers.parse('user enters username "{username}"'))
def enter_username(driver, username):

    page = LoginPage(driver)

    # Validation to avoid NoneType error
    assert username is not None
    assert username != ""

    page.enter_username(username)


# Enter Password
@when(parsers.parse('user enters password "{password}"'))
def enter_password(driver, password):

    page = LoginPage(driver)

    # Validation
    assert password is not None
    assert password != ""

    page.enter_password(password)


# Click Login Button
@when("user clicks login button")
def click_login(driver):

    page = LoginPage(driver)

    page.click_login()

    # Wait until next page loads
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )


# Verify Products Page
@then("user should see products page")
def verify_products_page(driver):

    assert "inventory" in driver.current_url