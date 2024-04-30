import pytest

from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def login(browser):
    login = LoginPage(browser)
    login.authorization()