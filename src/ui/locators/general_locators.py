from selenium.webdriver.common.by import By


class GeneralLocators:

    BACK = (By.CSS_SELECTOR, "div.segment:nth-child(1) > button:nth-child(1)")
    HOTP = (By.CSS_SELECTOR, "div.segment:nth-child(1) > button:nth-child(2)")
    TOTP = (By.CSS_SELECTOR, "div.segment:nth-child(1) > button:nth-child(3)")
    OCRA = (By.CSS_SELECTOR, "div.segment:nth-child(1) > button:nth-child(4)")
    EVV = (By.CSS_SELECTOR, "div.segment:nth-child(1) > button:nth-child(5)")

    ISSUER_FIELD = (By.ID, 'issuer')
    LABEL_FIELD = (By.ID, 'label')
    SECRET_BASE32_FIELD = (By.ID, 'secret-key')
    NEW_BASE32_BTN = (By.CSS_SELECTOR, 'div:nth-child(2) > button[onclick="newSecret()"]')
    SECRET_HEX_FIELD = (By.ID, 'secret-key-hex')
    NEW_HEX_BTN = (By.CSS_SELECTOR, 'div:nth-child(2) > button[onclick="newSecret()"]')
    ALGO_DROP = (By.ID, 'algorithm')
    LENGTH_FIELD = (By.ID, 'length')

    GENERATE_OTP_BTN = (By.CSS_SELECTOR, 'div button[type="submit"]')

    URI_FIELD = (By.ID, 'uri')
    COPY_URI_BTN = (By.CSS_SELECTOR, 'button[onclick="copyURIToClipboard()"]')

    FORMAT_BTN = (By.ID, "format")
    OTP = (By.ID, "otp")
    COPY_OTP_BTN = (By.CSS_SELECTOR, "div.segment:nth-child(2) > button:nth-child(3)")
    RANGE_FIELD = (By.ID, "range")
