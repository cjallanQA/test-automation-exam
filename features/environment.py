import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def _build_driver():
    options = ChromeOptions()
    if os.getenv("HEADLESS", "1") in {"1", "true", "TRUE", "yes", "YES"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver


def before_scenario(context, scenario):
    context.base_url = "https://the-internet.herokuapp.com"
    context.driver = _build_driver()


def after_scenario(context, scenario):
    if getattr(context, "driver", None):
        context.driver.quit()
