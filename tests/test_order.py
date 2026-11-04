import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
import allure
ORDER_DATA = [
    {
        "name": "Ева", "surname": "Петрова", "address": "ул. Ленина, 10",
        "metro": "Черкизовская", "phone": "+79991112233",
        "date": "14.05.2025", "rent": "сутки", "color": "black"
    },
    {
        "name": "Анна", "surname": "Сидорова", "address": "пр. Мира, 10",
        "metro": "Сокольники", "phone": "+79994445566",
        "date": "20.09.2026", "rent": "двое суток", "color": "grey"
    }
]

@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.parametrize("button_index, data", [
        (0, ORDER_DATA[0]),
        (1, ORDER_DATA[1]),
    ])

    def test_create_order(self, driver, button_index, data):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        if button_index == 0:
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

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
        page.click_order_button_top()
        page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.education-services.ru/"

    @allure.title("Проверка редиректа на Дзен по логотипу Яндекса")
    @allure.description("Кликаем по логотипу Яндекса, ждём открытия новой вкладки "
                        "и проверяем редирект на dzen.ru. Тест падает "
                        "из-за внешних уведомлений")
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        page.accept_cookies()

        original_window = driver.current_window_handle
        windows_before = driver.window_handles

        page.click_yandex_logo()

        WebDriverWait(driver, 15).until(
            lambda d: len(d.window_handles) > len(windows_before)
        )

        new_window = [w for w in driver.window_handles if w != original_window][0]
        driver.switch_to.window(new_window)

        try:
            button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(text(), 'Нет, спасибо')]") # редирект на яндекс заставляет его скачать
                )
            )
            driver.execute_script("arguments[0].click();", button)
        except Exception:
            pass

        WebDriverWait(driver, 20).until(
            lambda d: "dzen.ru" in d.current_url
        )
        assert "dzen.ru" in driver.current_url