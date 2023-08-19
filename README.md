﻿# Проект по Автоматизации тестирования с помощью Selenium и Python
**Написание промышленного кода через паттерн Page Object Model**
## ВАЖНО!!! Установка и запуск
* Если вы используете в Pycharm функцию Clone и вставляете ссылку на репозиторий проблем с установкой у вас не будет
* **Но если вы скачиваете проект, как ZIP архив, то после распаковки удалите "-master" из названия папки. 
Должно остаться в название только "AutoTest_Selenium_Project".**
*  В принципе Pycharm сам выдаст сообщение о подтягивание зависимостей из requirements.txt.
Но если вдруг этого не произошло, или вообще для подстраховки, используйте код: **pip install -r requirements.txt**
* Команды запуска
   * **pytest -v -s --tb=line test_main_page.py** и **pytest -v -s --tb=line test_product_page.py** 
   (language и browser_name заданы по умолчанию)
   * **pytest -v --tb=line -s -m login_guest** запуск тестов с маркировкой _login_guest_
   * **pytest -v --tb=line -s -m need_review** запуск тестов с маркировкой _need_review_

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