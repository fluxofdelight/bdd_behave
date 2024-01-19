from src.common.enum.buttons import Buttons
from src.common.enum.fields import Fields
from src.common.enum.pages import Pages
from src.common.enum.dropdowns import Dropdowns
from src.ui.locators.evv_locators import EVVLocators
from src.ui.locators.general_locators import GeneralLocators
from src.ui.locators.home_locators import HomeLocators
from src.ui.locators.hotp_locators import HOTPLocators
from src.ui.locators.ocra_locators import OCRALocators
from src.ui.locators.totp_locators import TOTPLocators


enum_pages = Pages
enum_buttons = Buttons
enum_fields = Fields
enum_dropdowns = Dropdowns
general = GeneralLocators
home = HomeLocators
totp = TOTPLocators
hotp = HOTPLocators
ocra = OCRALocators
evv = EVVLocators


all_buttons = {
    enum_buttons.BACK: general.BACK,
    enum_buttons.new_base32: general.NEW_BASE32_BTN,
    enum_buttons.new_hex: general.NEW_HEX_BTN,
    enum_buttons.increment: hotp.INCREMENT_BTN,
    enum_buttons.prev_month: evv.PREV_MONTH_BTN,
    enum_buttons.next_month: evv.NEXT_MONTH_BTN,
    enum_buttons.find_time: evv.FIND_TIME_BTN,
    enum_buttons.format: general.FORMAT_BTN,
    enum_buttons.copy_otp: general.COPY_OTP_BTN,
    enum_buttons.generate_otp: general.GENERATE_OTP_BTN,
    enum_buttons.repeat: totp.REPEAT_BTN,
    enum_buttons.copy_uri: general.COPY_URI_BTN
}

all_fields = {
    enum_fields.issuer: general.ISSUER_FIELD,
    enum_fields.label: general.LABEL_FIELD,
    enum_fields.secret_base32: general.SECRET_BASE32_FIELD,
    enum_fields.secret_hex: general.SECRET_HEX_FIELD,
    enum_fields.otp_length: general.LENGTH_FIELD,
    enum_fields.otp_lifetime: totp.INTERVAL_FIELD,
    enum_fields.counter: hotp.COUNTER_FIELD,
    enum_fields.challenge: ocra.CHALLENGE_FIELD,
    enum_fields.password: ocra.PASSWORD_FIELD,
    enum_fields.session: ocra.SESSION_FIELD,
    enum_fields.arrival_code: evv.ARRIVAL_FIELD,
    enum_fields.depart_code: evv.DEPART_FIELD
}

all_dropdowns = {
    enum_dropdowns.algorithm: general.ALGO_DROP,
    enum_dropdowns.interval: totp.INTERVAL_DROP,
    enum_dropdowns.format_challenge: ocra.FORMAT_CHALLENGE_DROP,
    enum_dropdowns.ocra_length: ocra.LENGTH_DROP,
    enum_dropdowns.challenge: ocra.CHALLENGE_DROP,
    enum_dropdowns.password: ocra.PASSWORD_DROP,
}

all_objects = [all_buttons, all_fields, all_dropdowns]
