from selenium.webdriver.common.by import By


class HomeLocators:

    HOTP_HOME = (By.CSS_SELECTOR, "ul > li:nth-child(1) > a")
    TOTP_HOME = (By.CSS_SELECTOR, "ul > li:nth-child(2) > a")
    OCRA_HOME = (By.CSS_SELECTOR, "ul > li:nth-child(3) > a")
    EVV_HOME = (By.CSS_SELECTOR, "ul > li:nth-child(4) > a")
    CONVERTER = (By.CSS_SELECTOR, "ul > li:nth-child(5) > a")
