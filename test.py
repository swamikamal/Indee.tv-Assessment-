import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProjectPage import ProjectPage
from pages.HomePage import HomePage

@pytest.fixture
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome()  # Or another driver if needed
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def project_page(driver):
    return ProjectPage(driver)

@pytest.fixture
def home_page(driver):
    return HomePage(driver)
