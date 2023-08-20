import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")
    time.sleep(2)
    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']//tbody//tr")
    row = len(row_elements)
    print("The No Of Row is :", row)
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']//tbody//tr//th")
    col = len(col_elements)
    print("The No Of Column is :", col)

    first_part = "//table[@id='customers']//tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path)
            # print(dynamic_path)
            print(data.text, end=" ")

            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                print(country_path)
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennet is in {country_text}")


