from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def test_vwologin():
    # SeleniumAPI - Creste session
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")
    signin_button_ele = driver.find_element(By.ID, "js-login-btn")
    email_address_ele.send_keys("das.dipak19@hotmail.com")
    password_ele.send_keys("Dipak12345@")
    signin_button_ele.click()

    # Explicit Wait
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-heading"))
    # )

    # Fluent Wait
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading"))
    # heading = driver.find_element(By.CSS_SELECTOR, ".page-heading")
    # print("The Element Text is :"+heading.text)
   # assert "Dashboard" in element.text

    driver.quit()

    # assert "Dashboard" in element.text
    # LOGGER.info("title is ->" + driver.title)
