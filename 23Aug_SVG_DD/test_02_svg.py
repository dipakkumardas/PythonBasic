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
    URL = "https://www.amcharts.com/svg-maps/?map=india"
    driver.get(URL)
    driver.maximize_window()
    actions = ActionChains(driver)
    time.sleep(5)
    # Flipkart  Login Button Close
    path_status = driver.find_elements(By.XPATH, "//*[local-name()='svg']/*[local-name()='g'][7]/*[local-name()='g']/*[local-name()='g']/*[local-name()='path']")
    for state in path_status:
        state_name = state.get_attribute("aria-label")
        print(state_name)
        if state_name == "West Bengal":
            actions.move_to_element(state).click().perform()
            break



