import allure
from selenium.webdriver.common.by import By

from resources.base import Base


class LumaNewCustomerPage(Base):

    def __init__(self):
        super().__init__()

        self._FIRST_NAME_FIELD_XPATH = '//*[@id="firstname"]'
        self._LAST_NAME_FIELD_XPATH = '//*[@id="lastname"]'
        self._EMAIL_FIELD_XPATH = '//*[@id="email_address"]'
        self._PASSWORD_FIELD_XPATH = '//*[@id="password"]'
        self._PASSWORD_CONFIRMATION_FIELD_XPATH = '//*[@id="password-confirmation"]'

        self._CREATE_ACCOUNT_BUTTON = "//button[@type='submit' and .//span[text()='Create an Account']]"

    @allure.step('Fill first name field')
    def _fill_first_name_field(self, text_to_write: str):
        self.helper.find_element(By.XPATH, self._FIRST_NAME_FIELD_XPATH).send_keys(text_to_write)

    @allure.step('Fill last name field')
    def _fill_last_name_field(self, text_to_write: str):
        self.helper.find_element(By.XPATH, self._LAST_NAME_FIELD_XPATH).send_keys(text_to_write)

    @allure.step('Fill email field')
    def _fill_email_field(self, text_to_write: str):
        self.helper.find_element(By.XPATH, self._EMAIL_FIELD_XPATH).send_keys(text_to_write)

    @allure.step('Fill password field')
    def _fill_password_field(self, text_to_write: str):
        self.helper.find_element(By.XPATH, self._PASSWORD_FIELD_XPATH).send_keys(text_to_write)

    @allure.step('Fill password confirmation field')
    def _fill_password_confirm_field(self, text_to_write: str):
        self.helper.find_element(By.XPATH, self._PASSWORD_CONFIRMATION_FIELD_XPATH).send_keys(text_to_write)

    @allure.step('Click on "Create an Account" button')
    def _click_create_account_button(self):
        self.helper.find_element(By.XPATH, self._CREATE_ACCOUNT_BUTTON).click()

    @allure.step('Fill register new user form and click submit button')
    def register_new_user(self, first_name: str, last_name: str, email: str, password: str, password_confirm: str):
        self._fill_first_name_field(first_name)
        self._fill_last_name_field(last_name)
        self._fill_email_field(email)
        self._fill_password_field(password)
        self._fill_password_confirm_field(password_confirm)
        self._click_create_account_button()
