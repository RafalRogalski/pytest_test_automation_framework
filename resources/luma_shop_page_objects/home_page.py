import allure
from selenium.webdriver.common.by import By

from resources.base import Base


class LumaHomePage(Base):

    def __init__(self):
        super().__init__()

        self._CREATE_ACCOUNT_BUTTON_XPATH = "//*[text()='Create an Account']"
        self._SIGN_IN_BUTTON_XPATH = "//*[text()='Sign In']"

    @allure.step('Click on "Create an Account" button')
    def click_create_account_button(self):
        self.helper.find_element(By.XPATH, self._CREATE_ACCOUNT_BUTTON_XPATH).click()

    @allure.step('Click on "Create an Account" button')
    def click_sign_in_button(self):
        self.helper.find_element(By.XPATH, self._SIGN_IN_BUTTON_XPATH).click()
