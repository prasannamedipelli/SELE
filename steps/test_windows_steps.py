from pytest_bdd import(
    scenarios,
    given,
    when,
    then
)

from pages.window_page import WindowPage

scenarios("../features/window_handle.feature")

@given("user opens window paractice page")
def open_window_page(driver):
    driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")


@when("user clicks open new window button")
def click_new_window(driver):
    page = WindowPage(driver)
    
    page.click_open_new_window()


@then("user switches to child window")
def seitch_child(driver, request):
    page = WindowPage(driver)
    parent = page.switch_to_child_window()
    request.config.parent_window = parent

@then("user verifies child window title")
def verify_title(driver):
    title = driver.title
    
    print("Child window title : " , title)
    assert "Window Handles Practice" in title
    

@then("user switces back to parent windows")
def switch_parent_window(driver, request):
    parent_window = request.config.parent_window
    driver.switch_to.window(parent_window)
   # driver.switch_to_window(parent_window)
    print("back to parent window welcome")