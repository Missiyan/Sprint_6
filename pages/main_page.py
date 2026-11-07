from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import DZEN_URL_PART

class MainPage(BasePage):
    def click_faq_question(self, index):
        questions = self.find_elements(MainPageLocators.FAQ_QUESTIONS)
        self.click_js_element(questions[index])
        self.wait.until(
            lambda d: self.find_elements(MainPageLocators.FAQ_ANSWERS)[index].is_displayed()
        )
    def get_faq_answer_text(self, index):
        answers = self.find_elements(MainPageLocators.FAQ_ANSWERS)
        return answers[index].text

    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
    
    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass

    def click_order_button(self, position):
        """position: 'top' или 'bottom'"""
        if position == "top":
            self.click(MainPageLocators.ORDER_BUTTON_TOP)
        else:
            self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_yandex_logo_and_switch_to_new_window(self):
        original_window = self.get_current_window_handle()
        windows_before = self.get_window_handles()
        self.click(MainPageLocators.YANDEX_LOGO)
        self.wait_for_new_window(windows_before)
        new_window = [w for w in self.get_window_handles() if w != original_window][0]
        self.switch_to_window(new_window)

    def wait_for_dzen_redirect(self, timeout=20):
        self.wait_for_url_contains(DZEN_URL_PART, timeout)