import allure
from locators.redirect_pages_locators import RedirectPageLocators
from pages.base_page import BasePage

class Redirect(BasePage):

    @allure.step('Клик на кнопку Восстановить Пароль')
    def click_recovery_password(self):
        self.click_to_element(RedirectPageLocators.RECOVER_PASSWORD)

    @allure.step('Клик на Личный кабинет')
    def click_my_cabinet(self):
        self.click_to_element(RedirectPageLocators.MY_CABINET)

    @allure.step('Клик на Историю Заказов')
    def click_orders_history(self):
        self.click_to_element(RedirectPageLocators.ORDERS_HISTORY)

    @allure.step('Клик на Выход в Личном Кабинете')
    def click_exit_my_cabinet(self):
        self.click_to_element(RedirectPageLocators.EXIT_MY_CABINET)