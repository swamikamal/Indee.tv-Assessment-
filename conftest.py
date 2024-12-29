# conftest.py
import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ProjectPage import ProjectPage


@pytest.fixture(scope="session")
def driver():
    # Initialize the WebDriver with the options
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()

@pytest.fixture(scope="session")
def login_page(driver):
    # Initialize login page without logging in automatically
    return LoginPage(driver)

@pytest.fixture(scope="session")
def logged_in_session(login_page):
    # Perform login once per session if needed
    login_page.open_page()
    login_page.login()
    assert login_page.is_logged_in(), "Failed to log in to the platform."

@pytest.fixture
def project_page(driver, logged_in_session):  # Ensures a logged-in session is available
    return ProjectPage(driver)

