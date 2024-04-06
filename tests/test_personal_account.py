from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import StellarBurgersLocators
from data import StellarBurgersTestData
import settings

class TestPersonalAccount:

    def test_enter_repsonal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.ARIA_CURRENT, 'Профиль'))

        area_current = driver.find_element(*StellarBurgersLocators.ARIA_CURRENT)

        assert area_current.is_displayed() and area_current.text == 'Профиль'

        driver.quit()

