from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import Data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self,locator):
        if Data.BROWSER_NAME == 'chrome':
            self.driver.find_element(*locator).click()
        else:
            WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click()", self.find_element_with_wait(locator))

    def enter_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_non_exist_element(self, locator):
        WebDriverWait(self.driver, 3).until_not(expected_conditions.presence_of_element_located(locator))

    def drag_and_drop_ff(self, source, target):
        self.driver.execute_script(Data.SCRIPT, source, target)

    def go_to_url(self, url):
        self.driver.get(url)