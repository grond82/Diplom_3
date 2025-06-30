import allure
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage

class RecoveryPasswordPage(BasePage):

    @allure.step('Ввод email')
    def input_email(self, email):
        self.enter_text_to_element(RecoveryPasswordPageLocators.FIELD_EMAIL, email)

    @allure.step('Клик на кнопку Восстановить пароль')
    def click_button_recovery(self):
        self.click_to_element(RecoveryPasswordPageLocators.BUTTON_RECOVER)

    @allure.step('Ввод пароля')
    def input_password(self, password):
        self.enter_text_to_element(RecoveryPasswordPageLocators.FIELD_PASSWORD, password)

    @allure.step('Сделать пароль видимым')
    def click_visible_password(self):
        self.click_to_element(RecoveryPasswordPageLocators.BUTTON_VISIBLE_PASSWORD)