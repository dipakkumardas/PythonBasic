from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


def test_vwologin2():
    # SeleniumAPI - Creste session
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    time.sleep(10)
    LOGGER.info("title is ->" + driver.title)
    linktext_ele = driver.find_element(By.LINK_TEXT, "Start a free trial")
    linktext_ele.click()
    
    # email_address_ele = driver.find_element(By.ID, "login-username")
    # password_ele = driver.find_element(By.NAME, "password")
    # signin_button_ele = driver.find_element(By.ID, "js-login-btn")
    # email_address_ele.send_keys("das.dipak19@hotmail.com")
    # password_ele.send_keys("Dipak12345@")
    # signin_button_ele.click()
    # time.sleep(10)
    # assert "Dashboard" in driver.title
    # LOGGER.info("title is ->" + driver.title)
    # 
    # driver.refresh()
    # driver.get("https://sdet.live")
    # driver.back()
    # driver.forward()
