import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()


def test_purchase_flow(driver):
    # Тест на покупку товара от авторизации до завершения покупки

    # Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Выбор товара и добавление в корзину
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    # Переход к оформлению заказа
    cart_page = CartPage(driver)
    cart_page.checkout()

    # Заполнение данных для оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Sandra", "Smit", "1776")
    checkout_page.complete_purchase()

    # Проверка успешного завершения покупки
    assert checkout_page.is_purchase_complete(), "Покупка не завершена успешно!"
