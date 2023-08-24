import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.wheel_actions import *


def test_04_window_handel():
    driver = webdriver.Chrome()
    driver.maximize_window()
    URL = "https://the-internet.herokuapp.com/windows"
    driver.get(URL)
    main_window_handel = driver.current_window_handle
    print(main_window_handel)
    link = driver.find_element(By.LINK_TEXT,"Click Here")
    link.click()

    window_handels = driver.window_handles
    print(window_handels)

    for handel in window_handels:
        driver.switch_to.window(handel)
        if "New Window" in driver.page_source:
            print("Found the text")
            break
        time.sleep(5)
    driver.switch_to.window(main_window_handel)
    time.sleep(10)
