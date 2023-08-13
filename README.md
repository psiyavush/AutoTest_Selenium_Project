# Проект по Автоматизации тестирования с помощью Selenium и Python
**Написание промышленного кода через паттерн Page Object Model**

## Файлы Тесты Проекта
* test_main_page.py - Тесты главной страницы
* test_product_page.py - Тесты страницы товара

## Основные файлы элементы Page Object
* pages/base_page.py - Базовая страница для проекта
* pages/main_page.py - Главная страница сайта
* pages/login_page.py - Страница входа/регистрации пользователя
* pages/product_page.py - Страница товара
* pages/basket_page.py - Страница корзины

## Вспомогательные файлы Проекта
* пустой файл __init__.py - чтобы работали относительные импорты (необязательно, но улучшает производительность)
* conftest.py - Файл хранения фикстур
* pages/locators.py - Здесь, внешние переменные для классов PageObject
* pytest.ini - файл для регистрации меток

