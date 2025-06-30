from selenium.webdriver.common.by import By

class LoginLocators:
    BUTTON_ENTER_TO_ACCOUNT = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")
    LOGIN_EMAIL_FIELD = (By.NAME, "name")
    LOGIN_PASSWORD_FIELD = (By.NAME, "Пароль")
    BUTTON_ENTER_ON_LOGIN_PAGE = (By.XPATH, ".//button[text()='Войти']")
    BUTTON_ORDER = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")