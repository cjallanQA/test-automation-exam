from behave import given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given("I open the-internet homepage")
def step_open_home_page(context):
    context.driver.get(context.base_url)
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "ul")))


@when('I open the "{link_text}" page from the homepage')
def step_navigate_to_page(context, link_text):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, link_text))
    ).click()
