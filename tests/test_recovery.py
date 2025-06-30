import allure
from url import TestUrl
from data import Data
from pages.recovery_password_page import RecoveryPasswordPage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators

class TestRecovery:

    @allure.title('Тест на ввод email и нажатия кнопки Восстановить')
    def test_enter_email_click_recovery_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.go_to_url(TestUrl.RECOVERY_PASSWORD_URL)
        recovery_page.input_email(Data.EMAIL)
        recovery_page.click_button_recovery()
        assert recovery_page.find_element_with_wait(RecoveryPasswordPageLocators.LOCATOR_FOR_TEST_ENTER_EMAIL).text == "Пароль"

    @allure.title('Тест на ввод пароля и сделать его видимым')
    def test_test_enter_password_and_visible(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.go_to_url(TestUrl.RECOVERY_PASSWORD_URL)
        recovery_page.input_email(Data.EMAIL)
        recovery_page.click_button_recovery()
        recovery_page.input_password(Data.PASSWORD)
        recovery_page.click_visible_password()
        assert recovery_page.find_element_with_wait(RecoveryPasswordPageLocators.FIELD_PASSWORD).get_attribute('type') == 'text'