import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.wheel_actions import *


def test_makemytrip():
    driver = webdriver.Chrome()
    URL = "https://www.makemytrip.com/"
    driver.get(URL)
    driver.maximize_window()
    fromCity = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).click().send_keys("New Delhi").perform()
    time.sleep(10)
