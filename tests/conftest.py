import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")

    options = webdriver.FirefoxOptions()
    options.page_load_strategy = 'normal'
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()

    yield browser
    print("\nquit browser..")
    browser.quit()
