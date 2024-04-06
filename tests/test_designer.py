from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import StellarBurgersLocators
from data import StellarBurgersTestData
import settings

class TestStellarBurgersDesigner:

    def test_select_filling(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TAB_FILING, 'Начинки'))


        driver.find_element(*StellarBurgersLocators.TAB_FILING).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_FILING, 'Начинки'))

        text_filing = driver.find_element(*StellarBurgersLocators.TEXT_FILING)

        assert text_filing.is_displayed() and text_filing.text == 'Начинки'

        driver.quit()


    def test_select_sauce(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TAB_SAUCE, 'Соусы'))

        driver.find_element(*StellarBurgersLocators.TAB_SAUCE).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_SAUCE, 'Соусы'))

        text_sause = driver.find_element(*StellarBurgersLocators.TEXT_SAUCE)

        assert text_sause.is_displayed() and text_sause.text == 'Соусы'

        driver.quit()

    def test_select_burgers(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_IN_ACCOUNT).click()

        driver.find_element(*StellarBurgersLocators.EMAIL_ACCOUNT).send_keys(StellarBurgersTestData.EMAIL)
        driver.find_element(*StellarBurgersLocators.PASSWORD_ACCOUNT).send_keys(StellarBurgersTestData.PASSWORD)

        driver.find_element(*StellarBurgersLocators.CORRECT).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TAB_FILING, 'Начинки'))

        driver.find_element(*StellarBurgersLocators.TAB_FILING).click()
        driver.find_element(*StellarBurgersLocators.TAB_BURGERS).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.TEXT_BURGERS, 'Булки'))

        text_burgers = driver.find_element(*StellarBurgersLocators.TEXT_BURGERS)

        assert text_burgers.is_displayed() and text_burgers.text == 'Булки'

        driver.quit()