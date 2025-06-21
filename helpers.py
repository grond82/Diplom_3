from url import TestUrl
from locators.login_locators import LoginLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Helpers:

    def login(self, driver):
        if Data.BROWSER_NAME == 'chrome':
            driver.get(TestUrl.HOMEPAGE_URL)
            driver.find_element(*LoginLocators.BUTTON_ENTER_TO_ACCOUNT).click()
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_EMAIL_FIELD))
            driver.find_element(*LoginLocators.LOGIN_EMAIL_FIELD).send_keys(Data.EMAIL)
            driver.find_element(*LoginLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.find_element(*LoginLocators.BUTTON_ENTER_ON_LOGIN_PAGE).click()
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(LoginLocators.BUTTON_ORDER))
        else:
            driver.get(TestUrl.HOMEPAGE_URL)
            driver.execute_script("arguments[0].click()", driver.find_element(*LoginLocators.BUTTON_ENTER_TO_ACCOUNT))
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_EMAIL_FIELD))
            driver.find_element(*LoginLocators.LOGIN_EMAIL_FIELD).send_keys(Data.EMAIL)
            driver.find_element(*LoginLocators.LOGIN_PASSWORD_FIELD).send_keys(Data.PASSWORD)
            driver.execute_script("arguments[0].click()", driver.find_element(*LoginLocators.BUTTON_ENTER_ON_LOGIN_PAGE))
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginLocators.BUTTON_ORDER))