# pages/HomePage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.logout_button = (By.XPATH, "//button[contains(text(),'Logout')]")

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button)).click()
