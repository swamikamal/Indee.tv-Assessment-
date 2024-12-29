#LoginPage.py
import logging
from selenium.webdriver.common.by import By
from pages.utils.selenium_utils import (
    wait_for_element_to_be_clickable,
    wait_for_element_to_be_present,
    wait_for_element_to_be_visible
)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.pin = 'WVMVHWBS'# this may have expired by the time
        self.url = "https://indeedemo-fyc.watch.indee.tv/"

        # Locators
        self.indee_image = (By.XPATH,'//*[@id="form-logo-image"]')
        self.input_pin = (By.XPATH, '//*[@id="access-code"]')
        self.sign_in_button = (By.XPATH,'//*[@id="sign-in-button"]')
        self.validation_text_page_title = (By.XPATH, '//*[@id="genre-sorter"]/div/div[1]/p')

    def open_page(self):
        self.driver.get(self.url)
        wait_for_element_to_be_visible(self.driver,self.indee_image)

    def enter_pin(self):
        wait_for_element_to_be_present(self.driver, self.input_pin).send_keys(self.pin)

    def submit(self):
        wait_for_element_to_be_clickable(self.driver, self.sign_in_button).click()

    def login(self):
        self.enter_pin()
        self.submit()

    def is_logged_in(self):
        try:
            wait_for_element_to_be_visible(self.driver, self.validation_text_page_title)
            return True
        except Exception as e:
            logging.error(f"Error while checking if logged in: {e}")
            return False
