import pytest
from pages.main_page import MainPage
import allure
FAQ_DATA = [
    (0, "Сутки — 400 рублей"),
    (1, "один заказ — один самокат"),
    (2, "Допустим, вы оформляете заказ на 8 мая"),
    (3, "Только начиная с завтрашнего дня"),
    (4, "Пока что нет!"),
    (5, "Самокат приезжает к вам с полной зарядкой"),
    (6, "Да, пока самокат не привезли"),
    (7, "Всем самокатов!"),
]

@allure.feature("Вопросы о важном")
class TestFaq:
    @pytest.mark.parametrize("index, expected_text", FAQ_DATA)
    def test_faq_answer(self, driver, index, expected_text):
        page = MainPage(driver)
        page.accept_cookies()
        page.click_faq_question(index)
        actual = page.get_faq_answer_text(index)
        assert expected_text in actual, f"Ожидали '{expected_text}' в ответе, получили: '{actual}'"