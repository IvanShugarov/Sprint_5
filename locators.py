from selenium.webdriver.common.by import By
# --- ГЛАВНАЯ СТРАНИЦА И ХЕДЕР ---
LOGIN_REG_BUTTON = (By.XPATH,".//div[@class='header_flexRow__Xdqv1']//button[text()='Вход и регистрация']")
MAIN_CREATE_AD_BUTTON = (By.XPATH,".//button[text()='Разместить объявление']")
MAIN_USER_AVATAR = (By.XPATH,".//button[@class='circleSmall']")
MAIN_USER_NAME_TEXT = (By.CSS_SELECTOR, ".profileText.name")
MAIN_EXIT_BUTTON = (By.XPATH,".//button[text()='Выйти']")

# --- МОДАЛЬНЫЕ ОКНА (ВХОД И РЕГИСТРАЦИЯ) ---
LOGIN_NO_ACCOUNT_BUTTON = (By.XPATH,".//div[@class='popUp_buttonRow__+W8JD']//button[text()='Нет аккаунта']")
LOGIN_EMAIL_INPUT = (By.NAME,"email")
LOGIN_PASSWORD_INPUT = (By.NAME,"password")
REG_CONFIRM_PASSWORD_INPUT  = (By.NAME,"submitPassword")

#--- ПОЛЯ РЕГИСТРАЦИИ ---
REG_CREATE_ACCOUNT_BUTTON  = (By.XPATH,".//div[@class='popUp_buttonRow__+W8JD']//button[text()='Создать аккаунт']")
LOGIN_MODAL_EMAIL_INPUT = (By.XPATH,".//input[@name='email']")
LOGIN_MODAL_PASSWORD_INPUT = (By.XPATH,".//input[@name='password']")
LOGIN_MODAL_SUBMIT_BUTTON = (By.XPATH,".//div[@class='popUp_buttonRow__+W8JD']//button[text()='Войти']")

#--- ОШИБКИ ВАЛИДАЦИИ --- 
REG_EMAIL_ERROR_MESSAGE = (By.XPATH,".//div/span[text()='Ошибка']")
REG_EMAIL_INPUT_ERROR = (By.XPATH,".//div[@class='input_inputError__fLUP9']//input[@name='email']")
REG_PASSWORD_INPUT_ERROR = (By.XPATH,".//div[@class='input_inputError__fLUP9']//input[@name='password']")
REG_CONFIRM_PASSWORD_INPUT_ERROR = (By.XPATH,".//div[@class='input_inputError__fLUP9']//input[@name='submitPassword']")

#--- МОДАЛКА ДЛЯ НЕАВТОРИЗОВАННЫХ --- 
MODAL_AUTH_REQUIRED_TITLE = (By.XPATH,".//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

#--- ФОРМА СОЗДАНИЯ ОБЪЯВЛЕНИЯ ---
AD_NAME_INPUT = (By.XPATH,".//div[@class='input_inputDefault__UmPK0']//input[@name='name']")
AD_PRICE_INPUT = (By.XPATH,".//div[@class='input_inputDefault__UmPK0']//input[@name='price']")
AD_DESCRIPTION_TEXTAREA = (By.XPATH,".//textarea")

#--- ДРОПДАУНЫ И ВЫБОР ЗНАЧЕНИЙ ---
AD_CATEGORY_DROPDOWN = (By.XPATH,".//input[@name='category']/following-sibling::button")
AD_CITY_DROPDOWN = (By.XPATH,".//input[@name='city']/following-sibling::button")
AD_CATEGORY_GARDENING = (By.XPATH,".//span[text()='Садоводство']")
AD_CITY_KAZAN = (By.XPATH,".//span[text()='Казань']")

#--- РАДИОКНОПКИ ---
AD_CONDITION_NEW_RADIO = (By.XPATH,".//input[@value='Новый']//following-sibling::div")
AD_CONDITION_USED_RADIO = (By.XPATH,".//input[@value='Б/У']//following-sibling::div")

#--- КНОПКА ПУБЛИКАЦИИ ---
AD_PUBLISH_BUTTON = (By.XPATH,".//button[text()='Опубликовать']")

#--- ЛИЧНЫЙ КАБИНЕТ ---
PROFILE_MY_ADS_TITLE = (By.XPATH,".//h1[@class='h1'and text()='Мои объявления']")
PROFILE_AD_NAME_BY_TEXT = (By.XPATH,".//div[@class='about']//h2")
