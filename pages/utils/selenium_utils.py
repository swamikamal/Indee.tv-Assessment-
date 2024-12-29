import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# time.sleep() is added to record the execution in the video.
def wait_for_element_to_be_clickable(driver, locator, timeout=10, delay=2):
    """Waits for an element to be clickable."""
    time.sleep(delay)
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_for_element_to_be_present(driver, locator, timeout=10, delay=2):
    """Waits for an element to be present in the DOM."""
    time.sleep(delay)
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def wait_for_element_to_be_visible(driver, locator, timeout=10, delay=2):
    """Waits for an element to be visible on the page."""
    time.sleep(delay)
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

# You can add more functions for different expected conditions as needed.
