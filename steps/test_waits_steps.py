from pytest_bdd import (
 scenarios,
 given,
 when,
 then   
)

from pages.wait_page import WaitsPage

scenarios("../features/wait.feature")

@given("user opens wait demo page")
def open_wait_page(driver):
    driver.get("https://www.hyrtutorials.com/p/waits-demo.html")
    
@when("user clicks add textbox1 button")
def click_button(driver):
    page = WaitsPage(driver=driver)
    page.click_add_textbox()
    
@then("textbox1 should appear")
def verify_textbox(driver):
    page = WaitsPage(driver)
    assert page.wait_for_text_box1()