from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_faq_question(self, index):
        questions = self.find_elements(MainPageLocators.FAQ_QUESTIONS)
        questions[index].click()

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

    def get_current_url(self):
        return self.driver.current_url
    
    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass
            