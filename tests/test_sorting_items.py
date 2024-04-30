import allure

from conftest import browser
from pages.base_page import BasePage
from pages.common_page import CommonPage
from pages.trade_page import TradePage


@allure.title("Продукты сортируются по максимальной цене")
def test_items_sorted_by_max_price(browser):
    base = BasePage(browser)
    common = CommonPage(browser)
    trade = TradePage(browser)

    base.go_to("/csgo/trade/")
    common.close_cooke_notification()
    trade.open_soring_list()

    trade.click_max_price()

    prices = trade.get_prices()
    prices_list = [float(price.text.replace('฿', '')) for price in prices]
    assert prices_list == sorted(prices_list, reverse=True), "Products are not sorted by max price"


@allure.title("Продукты сортируются по минимальной цене")
def test_items_sorted_by_min_price(browser):
    base = BasePage(browser)
    common = CommonPage(browser)
    trade = TradePage(browser)

    base.go_to("/csgo/trade/")
    common.close_cooke_notification()
    trade.open_soring_list()
    trade.click_min_price()
    new_prise = trade.get_prices()
    one = 1
    for i in new_prise:
        if i > new_prise[one]:
            one += 1
        else:
            return Exception("Products are not sorted by max price")


@allure.title("Продукты сортируются по максимальному урону")
def test_items_sorted_by_max_float(browser):
    base = BasePage(browser)
    common = CommonPage(browser)
    trade = TradePage(browser)

    base.go_to("/csgo/trade/")
    common.close_cooke_notification()
    trade.open_soring_list()
    trade.click_max_float()
    float_value = trade.get_floats()
    float_list = [float(float.text.replace('FN /', '')) for float in float_value]
    assert float_list == sorted(float_list, reverse=True), "Products are not sorted by max float"


@allure.title("Продукты сортируются по минимальному урону")
def test_items_sorted_by_min_float(browser):
    base = BasePage(browser)
    common = CommonPage(browser)
    trade = TradePage(browser)

    base.go_to("/csgo/trade/")
    common.close_cooke_notification()
    trade.open_soring_list()
    trade.click_min_float()
    new_prise = trade.get_floats()
    one = 1
    for i in new_prise:
        if i > new_prise[one]:
            one += 1
        else:
            return Exception("Products are not sorted by min float")
