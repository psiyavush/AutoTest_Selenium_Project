"""Каждый класс будет соответствовать каждому классу PageObject"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

