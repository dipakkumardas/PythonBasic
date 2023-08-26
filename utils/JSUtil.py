from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import  Alert


class JSUtils:

    def __init__(self,driver):
        self.driver = driver

    def make_alert(self,msg):
        js = self.driver.execute_script
        js("alert('" + msg + "')")