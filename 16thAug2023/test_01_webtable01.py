import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")
    time.sleep(2)
    row_element = driver.find_elements(By.XPATH, "//table[@id='customers']//tbody//tr")
    row = len(row_element)
    print("The No Of Row is :", row)
    col_element = driver.find_elements(By.XPATH, "//table[@id='customers']//tbody//tr//th")
    col = len(col_element)
    print("The No Of Column is :", col)
    driver.quit()
