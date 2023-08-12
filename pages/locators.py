"""Каждый класс будет соответствовать каждому классу PageObject"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, '//button[@value="Add to basket"]')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGES_PRODUCT_ADDED = (By.CSS_SELECTOR, 'div.alertinner strong')
    MESSAGES_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
