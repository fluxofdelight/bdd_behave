import logging as log
import time

from behave import *
from selenium.common import TimeoutException

from src.common import selenium_common as s
from src.common.enum.buttons import Buttons
from src.common.enum.fields import Fields
from src.common.enum.pages import Pages
from src.common.find_locator.find_locator import find_locator
from src.ui.locators.evv_locators import EVVLocators
from src.ui.locators.general_locators import GeneralLocators
from src.ui.locators.home_locators import HomeLocators
from src.ui.locators.hotp_locators import HOTPLocators
from src.ui.locators.ocra_locators import OCRALocators
from src.ui.locators.totp_locators import TOTPLocators


enum_pages = Pages
enum_buttons = Buttons
enum_fields = Fields
general = GeneralLocators
home = HomeLocators
totp = TOTPLocators
hotp = HOTPLocators
ocra = OCRALocators
evv = EVVLocators


@Step('I go to the "{page}" page')
def open_page(context, page):
    try:
        if page.upper() == enum_pages.TOTP:
            s.wait_and_click(context, home.TOTP_HOME, 1)
        elif page.upper() == enum_pages.HOTP:
            s.wait_and_click(context, home.HOTP_HOME, 1)
        elif page.upper() == enum_pages.OCRA:
            s.wait_and_click(context, home.OCRA_HOME, 1)
        elif page.upper() == enum_pages.EVV:
            s.wait_and_click(context, home.EVV_HOME, 1)
        elif page.capitalize() == enum_pages.converter:
            s.wait_and_click(context, home.CONVERTER, 1)
        else:
            raise Exception("Unknown page")
    except TimeoutException:
        home_page = "https://2fasolution.com/index.html"
        if not s.get_title(context, home_page):
            log.info("Required page is already opened")
            pass


@Step('the following data exist')
def collect_data(context):
    for key in context.table.headings:
        index = context.table.headings.index(key)
        if key == "issuer":
            context.issuer = context.table[0][index]
        elif key == "label":
            context.label = context.table[0][index]
        elif key == "secret":
            context.secret = context.table[0][index]
        elif key == "algorithm":
            context.algorithm = context.table[0][index]
        elif key == "otp_length_ocra":
            context.otp_length_ocra = context.table[0][index]


@Step('I click on the "{button}" button to turn it off')
@Step('I click on the "{button}" button to generate new OTP')
@Step('I click on the "{button}" button to generate new OTP and URI')
@Step('I click on the "{button}" button')
def click_button(context, button):
    locator = find_locator(button)
    return s.wait_and_click(context, locator)


@Step('I select the "{option}" in the "{dropdown}" drop-down')
def select_option(context, option, dropdown):
    locator = find_locator(dropdown)
    option = context.algorithm if option == "algorithm" else option
    option = context.otp_length_ocra if option == "otp_length_ocra" else option
    return s.wait_and_select_option_in_dropdown_by_value(context, locator, option)


@Step('I have already generated OTPs in the OTP range section')
def verify_otps_displaying_in_range(context):
    assert s.wait_and_get_attribute_text(context, general.RANGE_FIELD, "value"), \
        "OTPs are not generated in the range field"


@Step('I already have a generated OTP')
def verify_otp_displaying(context):
    assert s.wait_until_element_visible(context, general.OTP), "OTP is not generated"


@Step('I remember current OTP to make sure that new OTP generates')
def get_current_otp(context):
    context.otp = s.wait_and_get_text(context, general.OTP)
    return context.otp


@Step('I make sure that the new OTP generates')
def verify_next_otp_generation(context):
    old_otp = context.otp
    new_otp = get_current_otp(context)
    assert new_otp != old_otp, "New OTP hasn't generated"


@Step('I remember current URI to make sure that new URI generates')
def get_current_uri(context):
    context.uri = s.wait_and_get_attribute_text(context, general.URI_FIELD, "value")
    return context.uri


@Step('I make sure that the new URI generates')
def verify_new_uri_generation(context):
    old_uri = context.uri
    new_uri = get_current_uri(context)
    assert old_uri != new_uri, f"New URI hasn't generated. Old: {old_uri}\nNew: {new_uri}"


@Step('I make sure that the URI has this value')
def verify_uri(context):
    uri = get_current_uri(context)
    assert uri == context.text, f"Failed. Actual: {uri}\nExpected: {context.text}"


@Step('I wait until the next OTP period to be able to generate new one')
def wait_until_next_otp_period(context):
    otp_lifetime = s.wait_and_get_text(context, totp.PROGRESS_BAR)
    return time.sleep(int(otp_lifetime) + 0.5)


@Step('The default OTP Length is "{length}" digits')
def verify_default_otp_length(context, length):
    context.length = length
    actual_length = s.wait_and_get_attribute_text(context, general.LENGTH_FIELD, 'value')
    assert length == actual_length, f"Invalid default length. Actual: {actual_length}, expected: {length}"


@Step('I clear the "{field}" field')
def clear_field(context, field):
    locator = find_locator(field)
    return s.wait_and_clear_field(context, locator)


@Step('I enter the "{value}" in the "{field}" field')
def fill_in_field(context, field, value):
    locator = find_locator(field)
    value = context.issuer if value == "issuer" else value
    value = context.label if value == "label" else value
    value = context.secret if value == "secret" else value
    return s.wait_and_input(context, locator, value)


@Step('I clear the "{field}" field and enter the "{value}" in it')
def clear_and_fill_in_field(context, field, value):
    clear_field(context, field)
    return fill_in_field(context, field, value)


@Step('The "{element}" button becomes "{state}"')
@Step('The "{element}" button still has "{state}" state')
def check_element_state(context, element, state):
    locator = find_locator(element)
    if state.lower() == "active":
        assert not s.wait_and_verify_attribute(context, locator, "disabled", negative=True)
    elif state.lower() == "disabled":
        assert s.wait_and_verify_attribute(context, locator, "disabled")
    else:
        raise Exception("Invalid state. Can be 'active' or 'disabled'")


@Step('I make sure that new OTP "{have}" "{length}" length')
def verify_otp_length(context, have, length):
    length = 6 if length == "default" else length
    otp = ''.join(get_current_otp(context).split())
    if have.lower() == "has":
        assert len(otp) == int(length)
    elif have.lower() == "doesn't have":
        assert len(otp) != int(length)
    else:
        raise Exception("Invalid have. Can be 'has' or 'doesn't have'")
