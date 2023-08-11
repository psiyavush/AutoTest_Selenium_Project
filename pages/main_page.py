"""Класс связанный с главной страницей интернет-магазина"""
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Переходим на страницу логина"""
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        # символ *, указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        login_link.click()

    """Проверка ссылки на страницу логина"""
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

