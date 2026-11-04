from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_first_form(self, name, surname, address, metro, phone):
        self.input_text(OrderPageLocators.NAME_INPUT, name)
        self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)

        # ввести текст и выбрать станцию
        self.input_text(OrderPageLocators.METRO_INPUT, metro)
        self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_DROPDOWN_ITEM)
        ).click()

        self.input_text(OrderPageLocators.PHONE_INPUT, phone)

    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)


    def fill_second_form(self, date, rental_period, color, comment=""):
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ESCAPE)

        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENTAL_OPTION)

        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        else:
            self.click(OrderPageLocators.COLOR_GREY)

        if comment:
            self.input_text(OrderPageLocators.COMMENT_INPUT, comment)

    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_success_popup_visible(self):
        return self.wait_for_element_visible(OrderPageLocators.SUCCESS_POPUP).is_displayed()
        
    def get_success_message_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)