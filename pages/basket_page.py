"""Страница корзины"""
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверка, что товар в корзине
    def should_be_product_in_basket(self):
        assert self.browser.find_element(*BasketPageLocators.PRODUCT_IN_BASKET), 'Not a product in the basket'
        print("OK. A product in the basket")

    # Проверка, что товара нет в корзине
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'Error. A product in the basket'
        print("OK. Not a product in the basket")

    # Проверка, что есть сообщение о "пустой корзине"
    def should_be_message_about_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.MESSAGES_EMPTY_BASKET), 'Not message about empty basket'
        print('OK. Page has the message about empty basket')

    # Проверка, что нет сообщения о "пустой корзине"
    def should_not_be_message_about_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGES_EMPTY_BASKET), 'The message about empty basket'
        print("OK. Not message about empty basket")

