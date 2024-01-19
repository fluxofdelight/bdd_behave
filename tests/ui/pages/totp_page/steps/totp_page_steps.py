import time
import logging as log
from behave import *

from src.common.enum.buttons import Buttons
from src.ui.locators.general_locators import GeneralLocators
from src.ui.locators.totp_locators import TOTPLocators
from tests.ui.steps import general_steps
from src.common import selenium_common as s


general = GeneralLocators
totp = TOTPLocators
enum_buttons = Buttons


@Step('I have already pressed "{button}" button')
def verify_button_pressed(context, button):
    if button.upper() == enum_buttons.TOTP:
        assert s.wait_and_verify_attribute_text(context, general.TOTP, 'class', 'clicked'), \
            "Button is not pressed"
    elif button.capitalize() == enum_buttons.format:
        assert s.wait_and_verify_attribute_text(context, general.FORMAT_BTN, 'class', 'clicked'), \
            "Button is not pressed"
    elif button.capitalize() == enum_buttons.repeat:
        assert s.wait_and_verify_attribute_text(context, totp.REPEAT_BTN, 'class', 'clicked'), \
            "Button is not pressed"
    else:
        raise Exception("Unknown button")


@Step('Now the "{button}" button have an unpressed state')
def verify_button_not_pressed(context, button):
    if button.upper() == enum_buttons.TOTP:
        assert not s.wait_and_verify_attribute_text(context, general.TOTP, 'class', 'clicked'), \
            "Button is pressed"
    elif button.capitalize() == enum_buttons.format:
        assert not s.wait_and_verify_attribute_text(context, general.FORMAT_BTN, 'class', 'clicked'), \
            "Button is pressed"
    elif button.capitalize() == enum_buttons.repeat:
        assert not s.wait_and_verify_attribute_text(context, totp.REPEAT_BTN, 'class', 'clicked'), \
            "Button is pressed"
    else:
        raise Exception("Unknown button")


@Step('I have already progress bar with a timer')
def verify_progress_bar_changing(context):
    text1 = s.wait_and_get_attribute_text(context, totp.PROGRESS_BAR, 'style')
    time.sleep(1.5)
    text2 = s.wait_and_get_attribute_text(context, totp.PROGRESS_BAR, 'style')
    if text1 != text2:
        log.info('Progress bar is animated and it has a working timer')
        return True
    else:
        raise Exception("Progress bar is not animated and it does not have working timer")


@Step('The default OTP lifetime is "{interval}" seconds')
def verify_default_interval(context, interval='30'):
    context.interval = interval
    actual_interval = s.wait_and_get_selected_option_in_dropdown(context, totp.INTERVAL_FIELD)
    assert interval in actual_interval, f"Invalid default interval. Actual: {actual_interval}, expected: {interval}"


@Step('I wait until the next OTP will be generated')
def verify_next_otp_generation(context):
    old_otp = general_steps.get_current_otp(context)
    new_otp = general_steps.get_current_otp(context)
    while old_otp == new_otp:
        time.sleep(1)
        new_otp = general_steps.get_current_otp(context)
    else:
        assert new_otp != old_otp, "New OTP hasn't generated"
