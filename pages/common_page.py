import allure

from pages.base_page import BasePage
from actions import Actions
from locators import accept_cooke_banner, banner1, banner2


class CommonPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.action = Actions(browser)

    @allure.step("Закрыть баннер сохранения куки")
    def close_cooke_notification(self) -> None:
        self.action.click(accept_cooke_banner)

    @allure.step("Закрыть баннер с рекламмой")
    def close_banner1(self) -> None:
        self.action.click(banner1)

    @allure.step("Закрыть уведомление баннер с рекламмой")
    def close_banner2(self) -> None:
        self.action.click(banner2)
