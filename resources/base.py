import logging
from resources.driver_factory import DriverFactory
from resources.webdriver_helper import DriverHelper


class Base:
    """class that have all main variables to be inherited by page objects"""

    def __init__(self):
        self.loger = logging.getLogger()
        self.driver = DriverFactory.get_driver()
        self.helper = DriverHelper()
