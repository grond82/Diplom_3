from selenium.webdriver.common.by import By

class RedirectPageLocators:
    RECOVER_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    LOCATOR_FOR_TEST_REDIRECT_RECOVER_PASSWORD = By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]"
    MY_CABINET = By.XPATH, ".//p[contains(text(),'Личный Кабинет')]"
    PROFILE = By.XPATH, "//a[text()='Профиль']"
    ORDERS_HISTORY = By.XPATH, "//a[text()='История заказов']"
    LOCATOR_FOR_TEST_REDIRECT_ORDERS_HISTORY = By.XPATH, "//a[contains(@class, 'Account_link_active')]"
    EXIT_MY_CABINET = By.XPATH, ".//button[contains(text(), 'Выход')]"
    LOCATOR_FOR_TEST_EXIT_MY_CABINET = By.XPATH, ".//h2[contains(text(),'Вход')]"