import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Клик на Ленту Заказов')
    def click_orders_line(self):
        self.click_to_element(HomePageLocators.ORDERS_LINE)

    @allure.step('Клик на Конструктор')
    def click_constructor(self):
        self.click_to_element(HomePageLocators.CONSTRUCTOR)

    @allure.step('Клик на ингредиент')
    def click_ingredient(self, locator):
        self.click_to_element(locator)

    @allure.step('Закрыть окно Ингридиента')
    def click_close_ingredient(self):
        self.click_to_element(HomePageLocators.BUTTON_CLOSE_INGREDIENT)

    @allure.step('Перенести ингредиент')
    def drag_and_drop(self, source, target):
        source = self.find_element_with_wait(HomePageLocators.BUN_LOCATOR)
        target = self.find_element_with_wait(HomePageLocators.DROP_LOCATOR)
        self.drag_and_drop_ff(source, target)

    @allure.step('Закрыть окно заказа')
    def close_order(self):
        self.click_to_element(HomePageLocators.CLOSE_ORDER)

    @allure.step('Дождаться и получить номер заказа')
    def wait_and_get_order_number(self):
        element = self.find_element_with_wait(HomePageLocators.ORDER_NUMBER_LOCATOR)
        initial_number = element.text
        WebDriverWait(self.driver, 6).until_not(expected_conditions.text_to_be_present_in_element(HomePageLocators.ORDER_NUMBER_LOCATOR, initial_number))
        new_number = element.text
        self.close_order()
        return new_number