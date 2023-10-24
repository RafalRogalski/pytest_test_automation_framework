import logging

# Allure libraries
import allure
from allure_commons.types import AttachmentType

# Selenium libraries
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Other
from resources.driver_factory import DriverFactory
from resources.variables import Variables
from resources.drawing_on_screenshot import ScreenshotDrawer as Sd


class DriverHelper:
    """Class that provides common driver helpers with additionally screenshots every usage"""

    def __init__(self):
        self._driver = DriverFactory.get_driver()
        self._loger = logging.getLogger()

        super().__init__()

    def wait_for_element(self, by, locator) -> None | WebElement:
        try:
            element = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((by, locator)))
            self._loger.info(f"Found element by: {by} {locator}")
        except NoSuchElementException:
            self._loger.warning(f"Didn't found element by: {by} | {locator}")
            return None

        if Variables.ATTACH_SCREENSHOTS:
            screenshot = self._driver.get_screenshot_as_png()
            allure.attach(Sd(element, screenshot).get_screenshot(),
                          name=f"screenshot-element-locator {by} {locator}",
                          attachment_type=AttachmentType.JPG)

        return element

    def find_element(self, by, locator) -> None | WebElement:
        try:
            element = self._driver.find_element(by, locator)
            self._loger.info(f"Found element by: {by} {locator}")
        except NoSuchElementException:
            self._loger.warning(f"Didn't found element by: {by} | {locator}")
            return None

        if Variables.ATTACH_SCREENSHOTS:
            screenshot = self._driver.get_screenshot_as_png()

            allure.attach(Sd(element, screenshot).get_screenshot(),
                          name=f"screenshot-element-locator {by} {locator}",
                          attachment_type=AttachmentType.JPG)

        return element
