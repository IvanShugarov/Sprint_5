from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import generate_random_string

class TestAds:
    def test_create_ad_unauthorized_shows_modal(self,work_in_browser):
        work_in_browser.get("https://qa-desk.education-services.ru/")
        WebDriverWait(work_in_browser, 5).until(expected_conditions.visibility_of_element_located((MAIN_CREATE_AD_BUTTON)))
        work_in_browser.find_element(*MAIN_CREATE_AD_BUTTON).click()
        WebDriverWait(work_in_browser, 5).until(expected_conditions.visibility_of_element_located((MODAL_AUTH_REQUIRED_TITLE)))
        assert work_in_browser.find_element(*MODAL_AUTH_REQUIRED_TITLE).text == "Чтобы разместить объявление, авторизуйтесь"

    def test_create_ad_successful(self,authorized_user):
        authorized_user.find_element(*MAIN_CREATE_AD_BUTTON).click()
        element_name = authorized_user.find_element(*AD_NAME_INPUT)
        authorized_user.execute_script("arguments[0].scrollIntoView();",element_name)
        WebDriverWait(authorized_user, 5).until(expected_conditions.visibility_of_element_located((AD_NAME_INPUT)))
        ads_name =f"Горшок {generate_random_string()}"
        authorized_user.find_element(*AD_NAME_INPUT).send_keys(ads_name)
        element_price = authorized_user.find_element(*AD_PRICE_INPUT)
        authorized_user.execute_script("arguments[0].scrollIntoView();",element_price)
        authorized_user.find_element(*AD_CATEGORY_DROPDOWN).click()
        authorized_user.find_element(*AD_CATEGORY_GARDENING).click()
        authorized_user.find_element(*AD_CONDITION_USED_RADIO).click()
        authorized_user.find_element(*AD_CITY_DROPDOWN).click()
        authorized_user.find_element(*AD_CITY_KAZAN).click()
        authorized_user.find_element(*AD_DESCRIPTION_TEXTAREA).send_keys("Клёвый горшок")
        authorized_user.find_element(*AD_PRICE_INPUT).send_keys(100)
        authorized_user.find_element(*AD_PUBLISH_BUTTON).click()
        WebDriverWait(authorized_user, 5).until(expected_conditions.visibility_of_element_located((MAIN_USER_AVATAR)))
        authorized_user.find_element(*MAIN_USER_AVATAR).click()
        element_profile_ad_name = authorized_user.find_element(*PROFILE_MY_ADS_TITLE)
        authorized_user.execute_script("arguments[0].scrollIntoView();",element_profile_ad_name)
        WebDriverWait(authorized_user, 5).until(expected_conditions.visibility_of_element_located((PROFILE_MY_ADS_TITLE)))
        assert authorized_user.find_element(*PROFILE_AD_NAME_BY_TEXT).text == ads_name