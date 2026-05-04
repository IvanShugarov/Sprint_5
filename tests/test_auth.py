from locators import *
from helpers import generate_random_email
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAuth:
    def test_login_user(self,work_in_browser):
        work_in_browser.get("https://qa-desk.education-services.ru/")
        WebDriverWait(work_in_browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_REG_BUTTON)))
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
        work_in_browser.find_element(*MAIN_EXIT_BUTTON).click()
        WebDriverWait(work_in_browser,5).until(expected_conditions.visibility_of_element_located((LOGIN_REG_BUTTON)))
        work_in_browser.find_element(*LOGIN_REG_BUTTON).click()
        WebDriverWait(work_in_browser,5).until(expected_conditions.visibility_of_element_located((LOGIN_MODAL_EMAIL_INPUT)))
        work_in_browser.find_element(*LOGIN_MODAL_EMAIL_INPUT).send_keys(email)
        work_in_browser.find_element(*LOGIN_MODAL_PASSWORD_INPUT).send_keys("q")
        work_in_browser.find_element(*LOGIN_MODAL_SUBMIT_BUTTON).click()
        WebDriverWait(work_in_browser,5).until(expected_conditions.visibility_of_element_located((MAIN_EXIT_BUTTON)))
        assert work_in_browser.find_element(*MAIN_USER_NAME_TEXT).text == "User."
        assert work_in_browser.find_element(*MAIN_USER_NAME_TEXT).is_displayed()
    
    def test_logout_user(self,work_in_browser):
        work_in_browser.get("https://qa-desk.education-services.ru/")
        WebDriverWait(work_in_browser, 5).until(expected_conditions.visibility_of_element_located((LOGIN_REG_BUTTON)))
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
        work_in_browser.find_element(*MAIN_EXIT_BUTTON).click()
        WebDriverWait(work_in_browser,5).until(expected_conditions.visibility_of_element_located((LOGIN_REG_BUTTON)))
        assert work_in_browser.find_element(*LOGIN_REG_BUTTON).is_displayed()
        assert len(work_in_browser.find_elements(*MAIN_USER_AVATAR)) == 0