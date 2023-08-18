import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.negative
def test_01_IDrive_Login_test():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    #driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    # LOGGER.info("title is ->" + driver.title)
    username_ele = driver.find_element(By.XPATH, "//input[@id='username']")
    username_ele.send_keys("das.dipak19@hotmail.com")
    password_ele = driver.find_element(By.XPATH, "//input[@id='password']")
    password_ele.send_keys("dipak123")
    button = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    button.click()

    # LOGGER.info("title is ->" + driver.title)

    add_button = WebDriverWait(driver, 15).until(EC.visibility_of(driver.find_element(By.XPATH, "//a[@id='add-device-header-btn']")))
    add_button.click()

    # download_btn = driver.find_element(By.XPATH, "//*[@id='id-card-bdy-backup-agent-mac']/button")
    # download_btn.click()
   # page_title = driver.find_element(By.XPATH, "//title")
    # time.sleep(4)
    # assert "IDrive® 360 Backup Console for centralized management" in page_title
    # print("The Title of the page After Login"+page_title)
    # error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    # assert "Login failed! Please ensure the username and password are valid." in error_message.text
    # LOGGER.info("Invalid Login  Message  ->" + error_message.text)