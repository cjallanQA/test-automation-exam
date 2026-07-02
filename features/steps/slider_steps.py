from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def _current_slider_value(context):
    value = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, "range"))).text
    return float(value.strip())


@when('I set the slider to "{target_value}" using keyboard input')
def step_move_slider(context, target_value):
    target = float(target_value)
    slider = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='range']")))
    slider.click()
    for _ in range(40):
        current = _current_slider_value(context)
        if abs(current - target) < 0.001:
            return
        slider.send_keys(Keys.ARROW_RIGHT if current < target else Keys.ARROW_LEFT)
    raise AssertionError(f"Could not move slider to {target:.1f}")


@then('the slider value should be "{expected_value}"')
def step_verify_slider_value(context, expected_value):
    current = _current_slider_value(context)
    expected = float(expected_value)
    assert abs(current - expected) < 0.001, f"Expected {expected:.1f}, got {current:.1f}"
