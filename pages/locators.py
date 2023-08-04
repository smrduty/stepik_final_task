from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_FORM = (By.ID, "login_form")
    EMAIL_LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login-username"]')
    PASSWORD_LOGIN_INPUT = (By.CSS_SELECTOR, '[name="login-password"]')

    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTER_INPUT = (By.CSS_SELECTOR, '[name="registration-email"]')
    PASSWORD_REGISTER_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    PASSWORD_REGISTER_INPUT_AGAIN = (By.CSS_SELECTOR, '[name="registration-password2"]')
