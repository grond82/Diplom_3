import allure
from url import TestUrl
from pages.redirect_page import Redirect
from locators.redirect_pages_locators import RedirectPageLocators
from helpers import Helpers

class TestRedirect:

    @allure.title('Тест на редирект на страницу Восстановления пароля')
    def test_redirect_recovery_password_page(self, driver):
        driver.get(TestUrl.LOGIN_PAGE_URL)
        redirect_page = Redirect(driver)
        redirect_page.click_recovery_password()
        assert redirect_page.find_element_with_wait(RedirectPageLocators.LOCATOR_FOR_TEST_REDIRECT_RECOVER_PASSWORD).text == "Восстановление пароля"

    @allure.title('Тест на переход в Личный кабинет')
    def test_redirect_my_cabinet(self, driver):
        login = Helpers(driver)
        login.login(driver)
        redirect_page = Redirect(driver)
        redirect_page.click_my_cabinet()
        assert redirect_page.find_element_with_wait(RedirectPageLocators.PROFILE).text == "Профиль"

    @allure.title('Тест на переход в Историю заказов')
    def test_redirect_orders_history(self, driver):
        login = Helpers(driver)
        login.login(driver)
        redirect_page = Redirect(driver)
        redirect_page.click_my_cabinet()
        redirect_page.click_orders_history()
        assert 'Account_link_active' in redirect_page.find_element_with_wait(RedirectPageLocators.LOCATOR_FOR_TEST_REDIRECT_ORDERS_HISTORY).get_attribute('class')

    @allure.title('Тест на выход из моего кабинета')
    def test_exit_my_cabinet(self, driver):
        login = Helpers(driver)
        login.login(driver)
        redirect_page = Redirect(driver)
        redirect_page.click_my_cabinet()
        redirect_page.click_exit_my_cabinet()
        assert redirect_page.find_element_with_wait(RedirectPageLocators.LOCATOR_FOR_TEST_EXIT_MY_CABINET).text == "Вход"