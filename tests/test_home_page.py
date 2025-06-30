import allure
from url import TestUrl
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from helpers import Helpers
from locators.login_locators import LoginLocators

class TestHomePage:

    @allure.title('Тест на переход на Ленту Заказов')
    def test_click_orders_line(self,driver):
        homepage = HomePage(driver)
        homepage.go_to_url(TestUrl.HOMEPAGE_URL)
        homepage.click_orders_line()
        assert homepage.find_element_with_wait(HomePageLocators.LOCATOR_FOR_TESTING_ORDER_LINE).text == 'Лента заказов'

    @allure.title('Тест на переход на Конструктор')
    def test_click_constructor(self, driver):
        homepage = HomePage(driver)
        homepage.go_to_url(TestUrl.HOMEPAGE_URL)
        homepage.click_orders_line()
        homepage.click_constructor()
        assert homepage.find_element_with_wait(HomePageLocators.LOCATOR_FOR_TESTING_CONSTRUCTOR).text == 'Соберите бургер'

    @allure.title('Тест клик по ингредиенту')
    def test_click_ingredient(self, driver):
        homepage = HomePage(driver)
        homepage.go_to_url(TestUrl.HOMEPAGE_URL)
        homepage.click_ingredient(HomePageLocators.BUN_LOCATOR)
        assert homepage.find_element_with_wait(HomePageLocators.MODAL_INGREDIENT_LOCATOR).text == 'Детали ингредиента'

    @allure.title('Тест на закрытие окна ингредиента')
    def test_close_ingredient(self, driver):
        homepage = HomePage(driver)
        homepage.go_to_url(TestUrl.HOMEPAGE_URL)
        homepage.click_ingredient(HomePageLocators.BUN_LOCATOR)
        homepage.click_close_ingredient()
        assert homepage.wait_non_exist_element(HomePageLocators.LOCATOR_FOR_TESTING_CLOSE_INGREDIENTS) is None

    @allure.title('Тест на перенос ингредиента')
    def test_drag_and_drop_ingredient(self, driver):
        homepage = HomePage(driver)
        homepage.go_to_url(TestUrl.HOMEPAGE_URL)
        homepage.drag_and_drop(HomePageLocators.BUN_LOCATOR, HomePageLocators.DROP_LOCATOR)
        assert homepage.find_element_with_wait(HomePageLocators.COUNTER_LOCATOR_FOR_BUN).text == '2'

    @allure.title('Тест создания заказа')
    def test_create_order(self, driver):
        login = Helpers()
        login.login(driver)
        homepage = HomePage(driver)
        homepage.drag_and_drop(HomePageLocators.BUN_LOCATOR, HomePageLocators.DROP_LOCATOR)
        homepage.click_to_element(LoginLocators.BUTTON_ORDER)
        assert homepage.find_element_with_wait(HomePageLocators.LOCATOR_FOR_TESTING_CREATE_ORDER).text == 'идентификатор заказа'