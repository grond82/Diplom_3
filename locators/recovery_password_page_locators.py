from selenium.webdriver.common.by import By

class RecoveryPasswordPageLocators():
    FIELD_EMAIL = By.NAME, "name"
    BUTTON_RECOVER = By.XPATH, "//button[contains(text(), 'Восстановить')]"
    LOCATOR_FOR_TEST_ENTER_EMAIL = By.XPATH, "//label[contains(text(), 'Пароль')]"
    FIELD_PASSWORD = By.NAME, "Введите новый пароль"
    BUTTON_VISIBLE_PASSWORD = By.CSS_SELECTOR, "div.input__icon.input__icon-action"