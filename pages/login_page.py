import allure

from actions import Actions
from pages.base_page import BasePage
from locators import sign_in_by_steam, login_field, password_field, login_submit
from configs import test_steam_login, test_steam_password


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.action = Actions(browser)

    @allure.step("Авторизация")
    def authorization(self) -> None:
        self.action.click(*sign_in_by_steam)
        self.action.input(*login_field, text=test_steam_login)
        self.action.input(*password_field, text=test_steam_password)
        self.action.click(*login_submit)
