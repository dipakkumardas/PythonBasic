import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date


@pytest.mark.negative
def test_04_katalon_appointment_negativetest():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Explicit Wait -Wait For Element Make Appointment
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Make Appointment"))
    )

    LOGGER.info("title is ->" + driver.title)
    linktext_ele = driver.find_element(By.LINK_TEXT, "Make Appointment")
    linktext_ele.click()

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("John Doe")
    button = driver.find_element(By.ID, "btn-login")
    button.click()
    time.sleep(4)
    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed! Please ensure the username and password are valid." in error_message.text
    LOGGER.info("Invalid Login  Message  ->" + error_message.text)


@pytest.mark.positive
def test_03_katalon_appointment():
    # SeleniumAPI - Crest session
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Explicit Wait -Wait For Element Make Appointment
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Make Appointment"))
    )

    LOGGER.info("title is ->" + driver.title)
    linktext_ele = driver.find_element(By.LINK_TEXT, "Make Appointment")
    linktext_ele.click()

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    button = driver.find_element(By.ID, "btn-login")
    button.click()
    time.sleep(4)

    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")
    time.sleep(2)
    chckbox = driver.find_element(By.ID, "chk_hospotal_readmission")
    chckbox.click()
    time.sleep(2)
    radiobutton = driver.find_element(By.ID, "radio_program_medicaid")
    radiobutton.click()

    # Get Current Date
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%d/%m/%Y")
    print("Current date:", formatted_date)

    visitdate = driver.find_element(By.ID, "txt_visit_date")
    visitdate.send_keys(formatted_date)
    time.sleep(2)
    comment = driver.find_element(By.ID, "txt_comment")
    comment.send_keys("This is Booking For Testing Purpose")
    BookAppointment = driver.find_element(By.ID, "btn-book-appointment")
    BookAppointment.click()
    time.sleep(2)
    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in heading_h2.text
    LOGGER.info("Confirmation Heading is  ->" + heading_h2.text)

    BackToHome = driver.find_element(By.XPATH, "//a[contains(text(),'Go to Homepage')]")
    BackToHome.click()
    time.sleep(2)
