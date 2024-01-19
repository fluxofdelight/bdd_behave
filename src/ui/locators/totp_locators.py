from selenium.webdriver.common.by import By


class TOTPLocators:

    INTERVAL_DROP = (By.ID, "interval")
    INTERVAL_FIELD = (By.ID, "intervalValue")

    PROGRESS_BAR = (By.ID, "progress-bar")
    REPEAT_BTN = (By.ID, "repeat")
