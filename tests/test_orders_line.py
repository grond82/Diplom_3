import allure
from url import TestUrl
from pages.home_page import HomePage
from pages.orders_line_page import OrdersLinePage
from locators.orders_line_page_locators import OrdersPageLocators
from helpers import Helpers

class TestOrders:

    @allure.title('Тест на клик по заказу в Ленте Заказов')
    def test_order_from_order_line(self, driver):
        homepage = HomePage(driver)
        homepage.go_to_url(TestUrl.HOMEPAGE_URL)
        login = Helpers()
        login.login(driver)
        homepage.click_orders_line()
        orders_page = OrdersLinePage(driver)
        orders_page.click_on_order_order_line()
        assert orders_page.find_element_with_wait(OrdersPageLocators.ORDER_LOCATOR).text == 'Cостав'

    @allure.title('Тест на увеличение количества заказов за все время')
    def test_orders_all_time_increase(self, driver):
        orders_page = OrdersLinePage(driver)
        orders_page.go_to_url(TestUrl.HOMEPAGE_URL)
        login = Helpers()
        login.login(driver)
        old_orders, new_orders = orders_page.check_orders_all_time()
        assert new_orders > old_orders

    @allure.title('Тест на увеличение количества заказов за сегодня')
    def test_orders_today_increase(self, driver):
        orders_page = OrdersLinePage(driver)
        orders_page.go_to_url(TestUrl.HOMEPAGE_URL)
        login = Helpers()
        login.login(driver)
        old_orders, new_orders = orders_page.check_orders_today()
        assert new_orders > old_orders

    @allure.title('Тест на проверку заказа в работе')
    def test_order_in_work(self, driver):
        orders_page = OrdersLinePage(driver)
        orders_page.go_to_url(TestUrl.HOMEPAGE_URL)
        login = Helpers()
        login.login(driver)
        order_number, order_number_in_work = orders_page.check_order_numbers()
        order_number_in_work = order_number_in_work[1:]
        assert order_number == order_number_in_work

    @allure.title('Тест, что заказ есть в Ленте Заказов и в Истории Заказов')
    def test_order_in_order_line_and_my_orders(self, driver):
        orders_page = OrdersLinePage(driver)
        orders_page.go_to_url(TestUrl.HOMEPAGE_URL)
        login = Helpers()
        login.login(driver)
        order_line_number, my_order_number = orders_page.check_order_both_place()
        assert order_line_number == my_order_number