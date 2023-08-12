"""Каждый класс будет соответствовать каждому классу PageObject"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_REGISTER_FORM = (By.ID, 'register_form')
