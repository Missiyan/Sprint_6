import pytest
from pages.main_page import MainPage
import allure
from data import FAQ_DATA

@allure.feature("Вопросы о важном")
class TestFaq:
    @pytest.mark.parametrize("index, expected_text", FAQ_DATA)
    def test_faq_answer(self, driver, index, expected_text):
        page = MainPage(driver)
        page.accept_cookies()
        page.click_faq_question(index)
        assert page.get_faq_answer_text(index) == expected_text