from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    _driver = None

    @staticmethod
    def get_driver():
        return DriverFactory._driver_generator()

    @staticmethod
    def _driver_generator():
        if not DriverFactory._driver:
            options = webdriver.ChromeOptions()
            options.add_argument('--window-size=1600,1300')
            options.add_argument('--incognito')
            options.add_argument("--headless")

            DriverFactory._driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options)

        return DriverFactory._driver
