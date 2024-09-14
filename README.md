# E2E-UI 
## Тест для покупки товара на сайте [saucedemo.com](https://www.saucedemo.com)

## Описание

Этот проект представляет собой автоматический e2e тест для проверки сценария покупки товара на сайте [saucedemo.com](https://www.saucedemo.com) с использованием Python и Selenium. Тест проверяет процесс от авторизации до завершения покупки.

## Технологии

- **Python** 3.10
- **Selenium** для автоматизации взаимодействия с браузером
- **Pytest** для управления тестами
- **WebDriver Manager** для автоматического управления драйверами браузеров

## Структура проекта

```
E2E-UI/
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   └── test_purchase.py
├── utils/
│   ├── __init__.py
│   └── driver_setup.py
├── .gitignore
├── LICENSE
├── pytest.ini
├── README.md
└── requirements.txt
```
## Требования
- **[Python 3.10 или новее](https://www.python.org/downloads/)**
- **[Firefox](https://www.mozilla.org/ru/firefox/)**
- **Установленные зависимости (Selenium, Pytest, WebDriver Manager)**

## Установка

**1. Клонирование репозитория:**

```bash
git clone <https://github.com/Alexandra-Balabolkina/E2E-UI.git>
cd E2E-UI
```
**2. Создание и активация виртуального окружения:**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
```

**3. Установка зависимостей:**

```bash
pip install -r requirements.txt
```

Если у вас нет файла **requirements.txt**, вы можете создать его, добавив в него следующие строки:

```
selenium
pytest
webdriver-manager
```
## Запуск теста
Для запуска теста выполните следующую команду:

```bash
pytest tests/
```

Тест автоматически выполнит следующие шаги:

- Авторизуется на сайте [saucedemo.com](https://www.saucedemo.com) с использованием тестовых учетных данных.
- Выберет товар и добавит его в корзину.
- Перейдет к оформлению заказа.
- Заполнит поля с информацией и завершит покупку.
- Проверит, что покупка была успешно завершена.

## Настройка браузера
**По умолчанию тест использует Firefox.**
Если вы хотите использовать другой браузер, вам нужно изменить настройки в файле **driver_setup.py**.

