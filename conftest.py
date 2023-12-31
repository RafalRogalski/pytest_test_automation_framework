import allure
import pytest
from allure_commons.types import AttachmentType

from resources.base import Base
from resources.variables import Variables

base = Base()


@pytest.fixture(scope="function", autouse=True, name="Attach screenshot when test is failed")
def screenshot_on_fail(request):
    before_failed = request.session.testsfailed

    yield
    if request.session.testsfailed != before_failed:
        allure.attach(base.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)


@pytest.fixture(name="Go to luma test shop")
def go_to_luma_test_shop():
    base.driver.get(Variables.LUMA_TEST_SHOP_URL)


@pytest.fixture(name="Logout user from luma shop after test")
def logout_user_from_luma_shop_after_test():
    yield
    base.driver.get("https://magento.softwaretestingboard.com/customer/account/logout/")


@pytest.fixture(name="Logout user from luma shop before test")
def logout_user_from_luma_shop_before_test():
    base.driver.get("https://magento.softwaretestingboard.com/customer/account/logout/")


@pytest.fixture(scope="session", name="Session setup", autouse=True)
def session_setup():
    yield
    base.driver.close()


def pytest_addoption(parser):
    parser.addoption("--capture_screenshots", action="store", default="False", help="Options: True or False")


def get_allow_screenshot_flag(terminal_flag):
    if terminal_flag == "True" or terminal_flag == "true":
        return True
    else:
        return False


@pytest.fixture(scope="session", name="Screenshot flag set", autouse=True)
def screenshot_flag_fixture(request):
    my_variable = request.config.getoption("--capture_screenshots")
    Variables.ATTACH_SCREENSHOTS = get_allow_screenshot_flag(my_variable)
