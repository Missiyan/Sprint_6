import pytest
from selenium import webdriver
from data import BASE_URL

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(BASE_URL)
    yield driver
    driver.quit()