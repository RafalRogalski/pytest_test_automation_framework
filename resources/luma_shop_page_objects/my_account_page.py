import allure
from selenium.webdriver.common.by import By

from resources.base import Base


class LumaAccountPage(Base):

    def __init__(self):
        super().__init__()

        self._CONTACT_INFORMATION = ("//div[@class='box box-information' and .//span[text()='Contact Information']]")

    @allure.step("Retrieve contact information")
    def get_text_from_contact_information(self):
        return self.helper.find_element(By.XPATH, self._CONTACT_INFORMATION).text
