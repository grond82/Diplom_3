import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.orders_line_page_locators import OrdersPageLocators
from locators.home_page_locators import HomePageLocators
from locators.login_locators import LoginLocators
from locators.redirect_pages_locators import RedirectPageLocators
from pages.base_page import BasePage
from pages.home_page import HomePage

class OrdersLinePage(BasePage):

    @allure.step('Кликнуть на заказ в Ленте Заказов')
    def click_on_order_order_line(self):
        self.click_to_element(OrdersPageLocators.ORDER_LINE_FIRST_ORDER_LOCATOR)

    @allure.step('Количество заказов за все время')
    def orders_all_time(self):
        all_time_orders = self.find_element_with_wait(OrdersPageLocators.COMPLETE_ALL_TIME).text
        return all_time_orders

    @allure.step('Количество заказов за сегодня')
    def orders_today(self):
        today_orders = self.find_element_with_wait(OrdersPageLocators.COMPLETE_TODAY).text
        return today_orders

    @allure.step('Создание заказа и получение количества заказов за все время')
    def check_orders_all_time(self):
        homepage = HomePage(self.driver)
        homepage.click_orders_line()
        old_number = self.orders_all_time()
        homepage.click_constructor()
        homepage.drag_and_drop(HomePageLocators.BUN_LOCATOR, HomePageLocators.DROP_LOCATOR)
        homepage.click_to_element(LoginLocators.BUTTON_ORDER)
        homepage.wait_and_get_order_number()
        homepage.click_orders_line()
        new_number = self.orders_all_time()
        return old_number, new_number

    @allure.step('Создание заказа и получение количества заказов за сегодня')
    def check_orders_today(self):
        homepage = HomePage(self.driver)
        homepage.click_orders_line()
        old_number = self.orders_today()
        homepage.click_constructor()
        homepage.drag_and_drop(HomePageLocators.BUN_LOCATOR, HomePageLocators.DROP_LOCATOR)
        homepage.click_to_element(LoginLocators.BUTTON_ORDER)
        homepage.wait_and_get_order_number()
        homepage.click_orders_line()
        new_number = self.orders_today()
        return old_number, new_number

    @allure.step('Получить номер заказа в работе')
    def order_number_in_work(self):
        element = self.find_element_with_wait(OrdersPageLocators.ORDER_IN_WORK)
        initial_text = element.text
        WebDriverWait(self.driver, 6).until_not(expected_conditions.text_to_be_present_in_element(OrdersPageLocators.ORDER_IN_WORK, initial_text))
        order_number_in_work = self.find_element_with_wait(OrdersPageLocators.ORDER_IN_WORK).text
        return order_number_in_work

    @allure.step('Получение номера заказа и номера заказа в работе')
    def check_order_numbers(self):
        homepage = HomePage(self.driver)
        homepage.drag_and_drop(HomePageLocators.BUN_LOCATOR, HomePageLocators.DROP_LOCATOR)
        homepage.click_to_element(LoginLocators.BUTTON_ORDER)
        order_number = homepage.wait_and_get_order_number()
        homepage.click_orders_line()
        order_number_in_work = self.order_number_in_work()
        return order_number, order_number_in_work

    @allure.step('Получить номер последнего заказа из Истории Заказов')
    def get_number_last_order_orders_history(self):
        self.find_element_with_wait(OrdersPageLocators.ORDERS_IN_ORDER_HISTORY)
        my_orders = self.driver.find_elements(*OrdersPageLocators.ORDERS_IN_ORDER_HISTORY)
        last_element = my_orders[-2]
        last_number = last_element.text[2:]
        return last_number

    @allure.step('Получить номер последнего заказа из Ленты Заказов')
    def get_number_last_order_order_line(self):
        last_order = self.find_element_with_wait(OrdersPageLocators.ORDERS_IN_ORDER_HISTORY)
        first_number = last_order.text[2:]
        return first_number

    @allure.step('Получить номер последнего заказа из Истории Заказов и Ленты Заказов')
    def check_order_both_place(self):
        homepage = HomePage(self.driver)
        homepage.drag_and_drop(HomePageLocators.BUN_LOCATOR, HomePageLocators.DROP_LOCATOR)
        homepage.click_to_element(LoginLocators.BUTTON_ORDER)
        homepage.wait_and_get_order_number()
        homepage.click_orders_line()
        homepage.find_element_with_wait(OrdersPageLocators.ORDERS_IN_ORDER_HISTORY)
        order_line_number = self.get_number_last_order_order_line()
        self.click_to_element(RedirectPageLocators.MY_CABINET)
        self.click_to_element(OrdersPageLocators.ORDERS_HISTORY)
        my_order_number = self.get_number_last_order_orders_history()
        return order_line_number, my_order_number