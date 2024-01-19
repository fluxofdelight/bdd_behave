from selenium.webdriver.common.by import By


class OCRALocators:

    LENGTH_DROP = (By.ID, "length")
    FORMAT_CHALLENGE_DROP = (By.ID, "formatChallenge")

    CHALLENGE_FIELD = (By.ID, "question")
    CHALLENGE_DROP = (By.ID, "questionSettings")
    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_DROP = (By.ID, "passwordSettings")
    SESSION_FIELD = (By.ID, "sessionInformation")
