from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date


@pytest.mark.positive
def test_01_orange_hrm():
    # SeleniumAPI - Crest session
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Explicit Wait -Wait For Element Make Appointment
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h5[normalize-space()='Login']"))
    )
    LOGGER.info("title is ->" + driver.title)

    # Login Details
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("Admin")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("admin123")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    login_button.click()
    # Explicit Wait -Wait For Element Make Appointment
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-main-menu-item active']//span[1]"))
    )

    left_panel_admin = driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']//span[1]")
    left_panel_admin.click()
    time.sleep(9)




