from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersTestData
import random
class TestRegistration:

    def test_registration(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.LINK_REGISTER_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.REGISTER_NAME_ACCOUNT).send_keys(StellarBurgersTestData.NAME)
        driver.find_element(*StellarBurgersLocators.REGISTER_EMAIL_ACCOUNT).send_keys(f'treusilya7kogorta{random.randrange(100, 999)}@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTER_ACCOUNT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_ENTER, 'Вход'))
        text_enter = driver.find_element(*StellarBurgersLocators.TEXT_ENTER)


        assert text_enter.is_displayed() and text_enter.text == 'Вход'




    def test_registration_with_invalid_password(self, driver):

        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_REGISTER_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.REGISTER_NAME_ACCOUNT).send_keys(StellarBurgersTestData.NAME)
        driver.find_element(*StellarBurgersLocators.REGISTER_EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(
            StellarBurgersTestData.INVALID_PASSWORD)

        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTER_ACCOUNT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_ERROR_INCORRECT_PASSWORD, 'Некорректный пароль'))

        text_error_incorrect_password = driver.find_element(*StellarBurgersLocators.TEXT_ERROR_INCORRECT_PASSWORD)


        assert text_error_incorrect_password.is_displayed() and text_error_incorrect_password.text == 'Некорректный пароль'