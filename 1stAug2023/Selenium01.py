from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://app.vwo.com")
browser.close()
