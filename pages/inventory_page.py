from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-onesie')
        self.cart_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_to_cart(self):
        # Добавление товара в корзину
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        # Переход в корзину
        self.driver.find_element(*self.cart_icon).click()
