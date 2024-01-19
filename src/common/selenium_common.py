from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


default_timeout = 5


def open_url(context, url):
    context.driver.get(url)


def get_title(context, title):
    return context.driver.title == title


def wait_and_input(context, locator, value, timeout=default_timeout):
    message = f'Element with locator "{locator}" is not visible, after waiting {timeout} seconds.'
    return WebDriverWait(context.driver, timeout).until(
        EC.visibility_of_element_located(locator), message).send_keys(value)


def wait_and_clear_field(context, locator, timeout=default_timeout):
    message = f'Element with locator "{locator}" is not visible, after waiting {timeout} seconds.'
    return WebDriverWait(context.driver, timeout).until(EC.visibility_of_element_located(locator), message).clear()


def wait_and_click(context, locator, timeout=default_timeout):
    message = f'Element with locator "{locator}" is not clickable, after waiting {timeout} seconds.'
    return WebDriverWait(context.driver, timeout).until(EC.visibility_of_element_located(locator), message).click()


def wait_and_get_text(context, locator, timeout=default_timeout) -> str:
    message = f'Element with locator "{locator}" is not visible, after waiting {timeout} seconds.'
    text = WebDriverWait(context.driver, timeout).until(EC.visibility_of_element_located(locator), message).text
    return text


def wait_until_text_displayed(context, locator, text, timeout=default_timeout):
    message = f'Element with locator "{locator}" does not contain text "{text}", after waiting {timeout} seconds.'
    return WebDriverWait(context.driver, timeout).until(EC.text_to_be_present_in_element(locator, text), message)


def wait_until_element_visible(context, locator, timeout=default_timeout):
    message = f'Element with locator "{locator}" is not visible, after waiting {timeout} seconds.'
    if WebDriverWait(context.driver, timeout).until(EC.visibility_of_element_located(locator), message):
        return True
    else:
        return False


def wait_and_check_presence(context, locator, timeout=default_timeout):
    message = f'Element with locator "{locator}" is not present, after waiting {timeout} seconds.'
    if WebDriverWait(context.driver, timeout).until(EC.presence_of_element_located(locator), message):
        return True
    else:
        return False


def wait_and_get_all_elements(context, locator, timeout=default_timeout) -> list:
    message = f'Unable to find element with locator "{locator}", after waiting {timeout} seconds.'
    elements = WebDriverWait(context.driver, timeout).until(EC.visibility_of_all_elements_located(locator), message)
    return elements


def wait_and_get_attribute_text(context, locator, attribute, timeout=default_timeout):
    message = f'Unable to find element with locator "{locator}", after waiting {timeout} seconds.'
    text = WebDriverWait(context.driver, timeout).until(
            EC.visibility_of_element_located(locator), message).get_attribute(attribute)
    return text


def wait_and_verify_attribute_text(context, locator, attribute, expected_attr_text, timeout=default_timeout):
    actual_attr_text = wait_and_get_attribute_text(context, locator, attribute, timeout)
    if expected_attr_text in actual_attr_text:
        return True
    else:
        return False


def wait_and_verify_attribute(context, locator, attribute, negative=False, timeout=default_timeout) -> bool:
    message = (f"'Element with locator '{locator}' doesn't have attribute '{attribute}', "
               f"after waiting {timeout} seconds.'")
    if not negative:
        return WebDriverWait(context.driver, timeout).until(
            EC.element_attribute_to_include(locator, attribute), message
        )
    else:
        return WebDriverWait(context.driver, timeout).until_not(
            EC.element_attribute_to_include(locator, attribute), message
        )


def wait_and_get_property(context, locator, _property, timeout=default_timeout):
    message = f'Unable to find element with locator "{locator}", after waiting {timeout} seconds.'
    text = WebDriverWait(context.driver, timeout).until(
            EC.visibility_of_element_located(locator), message).get_property(_property)
    return text


def wait_and_get_selected_option_in_dropdown(context, locator, timeout=default_timeout):
    message = f'Unable to find element with locator "{locator}", after waiting {timeout} seconds.'
    dropdown_elements = WebDriverWait(context.driver, timeout).until(EC.visibility_of_element_located(locator), message)
    selected_option = Select(dropdown_elements).first_selected_option.text
    return selected_option


def wait_and_select_option_in_dropdown_by_value(context, locator, option_name, timeout=default_timeout):
    message = f'Unable to find element with locator "{locator}", after waiting {timeout} seconds.'
    dropdown_elements = WebDriverWait(context.driver, timeout).until(EC.visibility_of_element_located(locator), message)
    return Select(dropdown_elements).select_by_value(option_name)
