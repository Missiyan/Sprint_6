import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.delete_all_cookies() 
    driver.get("https://qa-scooter.education-services.ru/")
    yield driver
    driver.quit()
