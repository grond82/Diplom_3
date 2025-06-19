from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDERS_LINE = By.XPATH, "//p[contains(text(), 'Лента Заказов')]"
    LOCATOR_FOR_TESTING_ORDER_LINE = By.XPATH, "//h1[contains(text(), 'Лента заказов')]"
    CONSTRUCTOR = By.XPATH, "//p[contains(text(), 'Конструктор')]"
    LOCATOR_FOR_TESTING_CONSTRUCTOR = By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"
    BUN_LOCATOR = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"
    MODAL_INGREDIENT_LOCATOR = By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]"
    BUTTON_CLOSE_INGREDIENT = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    LOCATOR_FOR_TESTING_CLOSE_INGREDIENTS = By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"
    DROP_LOCATOR = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]"
    COUNTER_LOCATOR_FOR_BUN = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div[1]/p"
    LOCATOR_FOR_TESTING_CREATE_ORDER = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]"
    ORDER_NUMBER_LOCATOR = By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]"
    CLOSE_ORDER = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]"