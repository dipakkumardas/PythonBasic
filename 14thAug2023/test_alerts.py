import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test_alerts_accept_testing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button = driver.find_element(By.XPATH, "//button[contains(text(),'JS Alert')]")
    button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(5)
    alert.accept()
    time.sleep(5)
    acceptalerttext = driver.find_element(By.XPATH, "//p[contains(text(),'You successfully clicked an alert')]")
    print(acceptalerttext.text)
    driver.quit()
