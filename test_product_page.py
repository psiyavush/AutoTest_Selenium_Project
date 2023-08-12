"""Тест добавление в корзину со страницы товара"""
import time
import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, number):
    # Ссылка на тест по заданию 4.3 step 2
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    # Ссылка на тест по заданию 4.3 step 3
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    # Тест с параметризацией - заданию 4.3 step 4
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
