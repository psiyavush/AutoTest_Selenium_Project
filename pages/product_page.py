"""Страница товара"""
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Добавление товара в корзину
    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click()
        print("Product added to basket")

    # Проверка название товара в сообщении о добавлении
    def should_be_message_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_about_adding = self.browser.find_element(*ProductPageLocators.MESSAGES_PRODUCT_ADDED).text
        assert product_name == message_about_adding, "No product's name in the message about adding"
        print("Product's name in the message about adding")

    # Проверка цены товара в сообщении со стоимостью корзины
    def should_be_message_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGES_BASKET_PRICE).text
        assert product_price == message_basket_total, "Wrong product's price added to basket"
        print("Product's price added to basket")

    # Проверка отсутствия сообщения об успешном добавлении товара
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_PRODUCT_ADDED), "Success message about adding"
        print('OK, No success message about adding')

    # Проверка, что сообщения об успешном добавлении товара исчезает
    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES_PRODUCT_ADDED), "Success message not disappeared"
        print('OK, success message disappeared')
