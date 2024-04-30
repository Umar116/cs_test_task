import time

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class Actions(BasePage):

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def click(self, *element):
        time.sleep(1)
        button = self.wait.until(
            EC.presence_of_element_located(*element)
        )
        button.click()

    def input(self, *element, text):
        input_value = self.wait.until(
            EC.visibility_of_element_located(*element)
        )
        input_value.send_keys(text)


