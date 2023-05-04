from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        checking_url = 'login'
        assert checking_url in self.browser.current_url, f'String {checking_url} not content in page address'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not found!"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        button.click()
