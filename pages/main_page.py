from .base_page import BasePage
from selenium.webdriver.common.by import By

"""Класс связанный с главной страницей интернет-магазина"""


class MainPage(BasePage):
    """Переходим на страницу логина"""
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    """Проверка ссылки на страницу логина"""
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

