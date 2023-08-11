"""Базовая страница, от которой будут унаследованы все остальные классы.
    В ней мы опишем вспомогательные методы для работы с драйвером"""
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    """Метод открытия страницы:"""
    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    """Метод перехвата исключения 'NoSuchElementException' """
    # 2 аргумента: как (how) искать (css, id, xpath и тд) и что (what) искать (строку-селектор)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

