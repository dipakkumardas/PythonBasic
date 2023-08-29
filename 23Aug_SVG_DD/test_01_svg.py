import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    # Read a File, Read from DB, Create Webdriver


@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://www.flipkart.com/"
    driver.get(URL)
    driver.maximize_window()
    #time.sleep(5)
    # Flipkart  Login Button Close
    button_cross = driver.find_element(By.XPATH, "//button[contains(text(),'x']")
    actions = ActionChains(driver)
    actions.move_to_element(button_cross).click().perform()
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("AC")

    search_svg_icon = driver.find_element(By.XPATH, "//*[local-name()='svg']/*[local-name()='g' and @fill-rule='evenodd']")
    actions = ActionChains(driver)
    actions.move_to_element(search_svg_icon).click().perform()
