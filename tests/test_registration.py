from locators import StellarBurgersLocators
from data import StellarBurgersTestData
import time
class TestRegistration:

    def test_registration(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.LINK_REGISTER_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.REGISTER_NAME_ACCOUNT).send_keys(StellarBurgersTestData.NAME)
        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTER_ACCOUNT).click()

        time.sleep(5)

        assert driver.find_element(*StellarBurgersLocators.CORRECT).is_displayed() and driver.find_element(*StellarBurgersLocators.CORRECT).text == 'Войти', 'registration failed'


        driver.quit()


    def test_registration_with_invalid_password(self, driver):

        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_REGISTER_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.REGISTER_NAME_ACCOUNT).send_keys(StellarBurgersTestData.NAME)
        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(
            StellarBurgersTestData.INVALID_PASSWORD)

        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTER_ACCOUNT).click()

        time.sleep(5)

        assert driver.find_element(*StellarBurgersLocators.TEXT_ERROR_INCORRECT_PASSWORD).is_displayed() and driver.find_element(*StellarBurgersLocators.TEXT_ERROR_INCORRECT_PASSWORD).text == 'Некорректный пароль'

        driver.quit()