import time

from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@then("I should see content as soon as the page loads")
def step_verify_initial_content(context):
    text = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".example"))
    ).text.strip()
    assert text, "Expected visible content on load"


@when("I scroll to load more content blocks")
def step_load_more_content(context):
    start = len(context.driver.find_elements(By.CSS_SELECTOR, ".jscroll-added"))
    for _ in range(8):
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.7)
        loaded = len(context.driver.find_elements(By.CSS_SELECTOR, ".jscroll-added"))
        if loaded > start:
            return
    raise AssertionError("No additional content loaded after scrolling")


@then("I should reach the last loaded content block")
def step_verify_end_of_loaded_content(context):
    blocks = context.driver.find_elements(By.CSS_SELECTOR, ".jscroll-added")
    assert blocks, "Expected at least one loaded block"
    last_block = blocks[-1]
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", last_block)
    assert last_block.is_displayed() and last_block.text.strip(), "Last loaded block is not visible"
