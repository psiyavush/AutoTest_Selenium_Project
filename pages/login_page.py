"""Проверка перехода на страницу логина"""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        get_url = self.browser.current_url
        assert "login" in get_url, 'url of login is wrong'
        print('Page of login is correct ')

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Not login form in the page'
        print('Login form in the page')

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), 'Not register form in the page'
        print('Register form in the page')
