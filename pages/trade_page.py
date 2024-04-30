import allure

from actions import Actions
from locators import trade_page_link, sort_list_button, user_max_prise_sort_item, trade_items_price, user_min_prise, \
    user_max_float, float_price, user_min_float
from pages.base_page import BasePage


class TradePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.action = Actions(browser)

    @allure.step("Открытие страницы обмена")
    def open_trade_page(self) -> None:
        self.action.click(*trade_page_link)

    @allure.step("Открытие список сортировки")
    def open_soring_list(self) -> None:
        self.action.click(sort_list_button)

    @allure.step("Кликнуть на сортировку по максимальной цене")
    def click_max_price(self) -> None:
        self.action.click(user_max_prise_sort_item)

    @allure.step("Кликнуть на сортировку по минимальной цене")
    def click_min_price(self) -> None:
        self.action.click(user_min_prise)

    @allure.step("Кликнуть на сортировку по максимальному урону")
    def click_max_float(self) -> None:
        self.action.click(user_max_float)

    @allure.step("Кликнуть на сортировку по минимальному урону")
    def click_min_float(self) -> None:
        self.action.click(user_min_float)

    @allure.step("Получить список цен")
    def get_prices(self):
        return self.browser.find_elements(*trade_items_price)

    @allure.step("Получить список урона")
    def get_floats(self):
        return self.browser.find_elements(*float_price)
