from url import TestUrl
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from data import Data

class Helpers(BasePage):

    def login(self, driver):
        driver.get(TestUrl.HOMEPAGE_URL)
        login = BasePage(driver)
        login.click_to_element(LoginLocators.BUTTON_ENTER_TO_ACCOUNT)
        login.find_element_with_wait(LoginLocators.LOGIN_EMAIL_FIELD)
        login.enter_text_to_element(LoginLocators.LOGIN_EMAIL_FIELD, Data.EMAIL)
        login.enter_text_to_element(LoginLocators.LOGIN_PASSWORD_FIELD, Data.PASSWORD)
        login.click_to_element(LoginLocators.BUTTON_ENTER_ON_LOGIN_PAGE)
        login.find_element_with_wait(LoginLocators.BUTTON_ORDER)