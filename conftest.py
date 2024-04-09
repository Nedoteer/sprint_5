import pytest
from selenium import webdriver
import settings

@pytest.fixture(scope = 'function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(1920, 1080)
    chrome_driver.get('https://stellarburgers.nomoreparties.site/')

    yield chrome_driver

    chrome_driver.quit()
