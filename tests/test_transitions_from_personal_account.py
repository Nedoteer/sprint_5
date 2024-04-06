from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import StellarBurgersLocators
from data import StellarBurgersTestData
import settings

class TestTransitionsFromPersonalAccount:

    def test_transitions_from_personal_account_in_click_designer(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_ENTER_DESIGNER).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_DESIGNER, 'Соберите бургер'))

        text_designer = driver.find_element(*StellarBurgersLocators.TEXT_DESIGNER)

        assert text_designer.is_displayed() and text_designer.text == 'Соберите бургер'

        driver.quit()


    def test_from_personal_account_in_click_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_ENTER_LOGO).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_DESIGNER, 'Соберите бургер'))

        text_designer = driver.find_element(*StellarBurgersLocators.TEXT_DESIGNER)

        assert text_designer.is_displayed() and text_designer.text == 'Соберите бургер'

        driver.quit()


