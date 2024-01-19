from selenium.webdriver.common.by import By


class EVVLocators:

    ARRIVAL_FIELD = (By.ID, "arrivalCode")
    DEPART_FIELD = (By.ID, "departureCode")

    PREV_MONTH_BTN = (By.ID, "prevMonth")
    NEXT_MONTH_BTN = (By.ID, "nextMonth")
    FIND_TIME_BTN = (By.CLASS_NAME, "w60")
