import logging

logging.basicConfig(level=logging.INFO)

def test_login(login_page):
    login_page.open_page()
    login_page.login()
    assert login_page.is_logged_in(), "Failed to log in to the platform."
