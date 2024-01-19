from selenium import webdriver
import logging as log
from behave import fixture, use_fixture

from src.configs.config import Config


@fixture
def start_browser(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")
    log.info("Stating 'Chrome' for UI tests...")
    context.driver = webdriver.Chrome(options=chrome_options)
    log.info("Browser started")
    context.driver.get(Config.base_url)
    return context.driver


def before_all(context):
    use_fixture(start_browser, context)


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()
    return context.driver.refresh()


def after_all(context):
    return context.driver.quit()
