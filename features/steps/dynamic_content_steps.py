from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def _row_texts(driver):
    rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content .row")))
    return [row.text.strip() for row in rows[:3]]


@when("I record the dynamic content rows")
def step_capture_rows(context):
    context.before_refresh_rows = _row_texts(context.driver)


@when("I refresh the page")
def step_refresh_page(context):
    context.driver.refresh()
    context.after_refresh_rows = _row_texts(context.driver)


@then("I should see which dynamic rows changed")
def step_identify_changed_rows(context):
    changed_rows = [i + 1 for i, (a, b) in enumerate(zip(context.before_refresh_rows, context.after_refresh_rows)) if a != b]
    assert changed_rows, "Expected at least one row to change after refresh"
    context.changed_rows = changed_rows
    print(f"Changed rows after refresh: {changed_rows}")
