# downs2811@gmail.com
# TEST123pass
from selenium.webdriver.common.by import By

LINK = 'https://www.dropbox.com'

class MainPageLocators():
    TITLE = 'Dropbox'
    SIGN_IN_LINK = (By.XPATH, "//span[contains(text(),'Войти')]")
    GET_STARTED_LINK = (By.XPATH, "//span[contains(text(),'Начать')]")
    CONTACT_SALES_DROPDOWN = (By.XPATH, "//span[contains(text(),'Contact sales')]")
    SUPPORT_DROPDOWN = (By.XPATH, "//span[contains(text(),'Support')]")
    PLANS_PRICING_LINK = (By.XPATH, "//span[contains(text(),'Plans & pricing')]")
    FEATURES_DROPDOWN = (By.XPATH, "//span[contains(text(),'Features')]")
    WHY_DROPBOX_DROPDOWN = (By.XPATH, "//span[contains(text(),'Features')]")
    LOGO_LINK = (By.CSS_SELECTOR, ".arbor-logo")
    POP_UP_WINDOW_SIGN_UP = (By.CSS_SELECTOR, ".RebrandHero-drawer-forms")

class PopUpSignInLocators():
    SIGN_IN_ACCOUNT_LINK = (By.CSS_SELECTOR, "#sign-in-link")
    # bla-bla

class MainLogInPage():
    # LINK = 'https://www.dropbox.com/login'
    EMAIL_FIELD = (By.CSS_SELECTOR, '.text-input-wrapper [name=login_email]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.text-input-wrapper [name=login_password]')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, '.login-button.signin-button.button-primary')
    CHECKBOX_REMEMBER_ME = (By.CSS_SELECTOR, '[name=remember_me]')
    LINK_FORGOT_PASSWORD = (By.CSS_SELECTOR, '.forgot-password-link')
    BUTTON_SIGN_IN_GOOGLE = (By.CSS_SELECTOR, '.login-form-container__google-div .sign-in-text')
    BUTTON_SIGN_IN_APPLE = (By.CSS_SELECTOR, '.login-form-container__apple-div .sign-in-text')
    LINK_CREATE_ACCOUNT = (By.XPATH, "//a[contains(text(),'create an account')]")