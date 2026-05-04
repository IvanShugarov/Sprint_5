import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import generate_random_email

@pytest.fixture
def work_in_browser(request):
    driver = webdriver.Chrome()
    def teardown():
        driver.quit()
    request.addfinalizer(teardown)
    return driver

@pytest.fixture
def authorized_user(work_in_browser):
    work_in_browser.get("https://qa-desk.education-services.ru/")
    WebDriverWait(work_in_browser, 5).until(expected_conditions.element_to_be_clickable((LOGIN_REG_BUTTON)))
    work_in_browser.find_element(*LOGIN_REG_BUTTON).click()
    WebDriverWait(work_in_browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_NO_ACCOUNT_BUTTON)))
    work_in_browser.find_element(*LOGIN_NO_ACCOUNT_BUTTON).click()
    WebDriverWait(work_in_browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_EMAIL_INPUT)))
    email = generate_random_email()
    work_in_browser.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    work_in_browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys("q")
    work_in_browser.find_element(*REG_CONFIRM_PASSWORD_INPUT).send_keys("q")
    work_in_browser.find_element(*REG_CREATE_ACCOUNT_BUTTON).click()
    WebDriverWait(work_in_browser,5).until(expected_conditions.visibility_of_element_located((MAIN_USER_AVATAR)))
    return work_in_browser