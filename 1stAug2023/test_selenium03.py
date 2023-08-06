import pytest
from selenium import webdriver
import logging


def test_login():
    # Chrome --> Chrome Option
    chrome_options = webdriver.ChromeOptions()
    # extension_path = "G:/CRX/adblocker1.crx"
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument('--headless=new')
    # chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome(chrome_options)
    # driver.maximize_window()
    driver.get("https://app.vwo.com")
