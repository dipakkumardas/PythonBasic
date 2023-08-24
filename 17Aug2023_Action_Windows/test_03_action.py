import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.wheel_actions import *


def test_03_Actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver).double_click(clickable).perform()
    time.sleep(6)
    driver.close()


def test_hover_Action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    hoverable = driver.find_element(By.ID, "hover")
    ActionChains(driver).move_to_element(hoverable).perform()
    time.sleep(6)
    driver.close()


def test_drag_drop_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")
    ActionChains(driver).drag_and_drop(draggable, droppable).perform()
    time.sleep(10)
    driver.close()


def test_scroll_action():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    # Scroll Element with Offset Acmount 0, -50

    scroll_origin = ScrollOrigin.from_element(iframe)

    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 200).perform()

    time.sleep(10)
    driver.close()
