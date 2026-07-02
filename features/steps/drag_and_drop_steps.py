from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@when("I swap box A with box B")
def step_swap_boxes(context):
    script = """
    const [src, dst] = arguments;
    const data = new DataTransfer();
    src.dispatchEvent(new DragEvent('dragstart', { dataTransfer: data }));
    dst.dispatchEvent(new DragEvent('drop', { dataTransfer: data }));
    src.dispatchEvent(new DragEvent('dragend', { dataTransfer: data }));
    """

    box_a = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, "column-a")))
    box_b = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.ID, "column-b")))

    context.driver.execute_script(script, box_a, box_b)


@then('the left column header should be "{expected}"')
def step_verify_box_a_label(context, expected):
    header = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-a header"))
    )
    assert header.text.strip() == expected, (
        f"Expected column A to show '{expected}', but got '{header.text.strip()}'"
    )


@then('the right column header should be "{expected}"')
def step_verify_box_b_label(context, expected):
    header = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-b header"))
    )
    assert header.text.strip() == expected, (
        f"Expected column B to show '{expected}', but got '{header.text.strip()}'"
    )
