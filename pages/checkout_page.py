from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        # Инициализация драйвера и элементов страницы
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, 'complete-header')

    def fill_checkout_info(self, first_name, last_name, postal_code):
        # Заполнение полей для оформления заказа
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def complete_purchase(self):
        # Завершение покупки
        self.driver.find_element(*self.finish_button).click()

    def is_purchase_complete(self):
        # Проверка успешного завершения покупки
        complete_text = self.driver.find_element(*self.complete_header).text
        print(f"Текст завершения покупки: {complete_text}")
        return "Thank you for your order!" in complete_text
