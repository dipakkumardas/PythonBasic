import pytest
from selenium import webdriver
import logging


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is information Logs")
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is warning Logs")
    LOGGER.error("This is error Logs")
    LOGGER.critical("This is critical Logs")
    print(driver.title)
    assert "Login - VWO" in driver.title
