from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, 'checkout')

    def checkout(self):
        # Переход к оформлению заказа
        self.driver.find_element(*self.checkout_button).click()
