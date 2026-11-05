import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure
from data import ORDER_DATA, BASE_URL, DZEN_URL_PART

@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.parametrize("position, data", [
        ("top", ORDER_DATA[0]),
        ("bottom", ORDER_DATA[1]),
    ])
    def test_create_order(self, driver, position, data):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button(position)

        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.fill_first_form(
            data["name"], data["surname"], data["address"], data["metro"], data["phone"]
        )
        order_page.click_next()
        order_page.fill_second_form(data["date"], data["rent"], data["color"])
        order_page.click_order()
        order_page.confirm_order()

        assert order_page.is_success_popup_visible()
        assert "Заказ оформлен" in order_page.get_success_message_text()

    def test_scooter_logo_redirects_to_main(self, driver):
        page = MainPage(driver)
        page.accept_cookies()
        page.click_order_button("top")
        page.click_scooter_logo()
        assert page.get_current_url() == BASE_URL

    @allure.description("Кликаем по логотипу Яндекса, ждём открытия новой вкладки ")
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.accept_cookies()
        page.click_yandex_logo_and_switch_to_new_window()
        #page.close_yandex_browser_promo_if_present()
        page.wait_for_dzen_redirect()
        assert DZEN_URL_PART in page.get_current_url()