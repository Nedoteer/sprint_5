from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import StellarBurgersLocators
from data import StellarBurgersTestData
import settings

class TestStellarBurgersLogIn:

    def test_log_in(self, driver):

        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.MAKE_ORDER_BUTTON, 'Оформить заказ'))

        button_name = driver.find_element(*StellarBurgersLocators.MAKE_ORDER_BUTTON)

        assert button_name.is_displayed() and button_name.text == 'Оформить заказ'



    def test_log_in_button_personal_account(self, driver):

        driver.find_element(*StellarBurgersLocators.BUTTON_PERSSONAL_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.MAKE_ORDER_BUTTON,
                                                              'Оформить заказ'))

        button_name = driver.find_element(*StellarBurgersLocators.MAKE_ORDER_BUTTON)

        assert button_name.is_displayed() and button_name.text == 'Оформить заказ'



    def test_log_in_use_link_registration_form(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_REGISTER_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_ENTER_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.MAKE_ORDER_BUTTON,
                                                              'Оформить заказ'))

        button_name = driver.find_element(*StellarBurgersLocators.MAKE_ORDER_BUTTON)

        assert button_name.is_displayed() and button_name.text == 'Оформить заказ'



    def test_log_in_use_link_in_password_reset_form(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_FORGOT_PASSWORD).click()
        driver.find_element(*StellarBurgersLocators.LINK_ENTER_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.MAKE_ORDER_BUTTON,
                                                              'Оформить заказ'))

        button_name = driver.find_element(*StellarBurgersLocators.MAKE_ORDER_BUTTON)

        assert button_name.is_displayed() and button_name.text == 'Оформить заказ'







