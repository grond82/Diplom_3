from selenium.webdriver.common.by import By

class OrdersPageLocators:
    ORDER_LINE_FIRST_ORDER_LOCATOR = By.XPATH, "//a[contains(@class, 'OrderHistory_link')]"
    ORDER_LOCATOR = By.XPATH, "//p[contains(text(), 'Cостав')]"
    COMPLETE_ALL_TIME = By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::*"
    COMPLETE_TODAY = By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::*"
    ORDER_IN_WORK = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"
    ORDERS_HISTORY = By.XPATH, "//a[contains(text(), 'История заказов')]"
    ORDERS_IN_ORDER_HISTORY = By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]"