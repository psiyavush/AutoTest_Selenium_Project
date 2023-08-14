"""Каждый класс будет соответствовать каждому классу PageObject"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_1 = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.XPATH, '//button[@value="Register"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, '//button[@value="Add to basket"]')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGES_PRODUCT_ADDED = (By.CSS_SELECTOR, 'div.alertinner strong')
    MESSAGES_BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    MESSAGES_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p:first-child')
