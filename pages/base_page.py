from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass

    def click_js_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def wait_for_new_window(self, windows_before, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(windows_before)
        )

    def wait_for_url_contains(self, url_part, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part in d.current_url
        )