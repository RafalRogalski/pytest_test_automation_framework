import pytest
import allure

from resources.customer import Customer
from resources.luma_shop_page_objects.home_page import LumaHomePage
from resources.luma_shop_page_objects.create_new_customer_page import LumaNewCustomerPage
from resources.luma_shop_page_objects.my_account_page import LumaAccountPage


@allure.parent_suite("UI")
@allure.suite("Basic suites")
class TestUserRegistrationLumaShop:
    customer: Customer = None
    luma_home_page = LumaHomePage()
    luma_new_customer_page = LumaNewCustomerPage()
    luma_account_page = LumaAccountPage()

    @pytest.fixture(name="Customer creation fixture", autouse=True)
    def customer_creation(self):
        self.customer = Customer()

    @pytest.mark.usefixtures("Go to luma test shop",
                             "Customer creation fixture",
                             "Logout user from luma shop after test")
    @allure.sub_suite("01 Registration suite")
    @allure.description("Test of creating new user by using valid data for luma test shop")
    @allure.title("01 Registration test using valid data")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_register_new_user(self):
        self.luma_home_page.click_create_account_button()
        self.luma_new_customer_page.register_new_user(first_name=self.customer.first_name,
                                                      last_name=self.customer.last_name,
                                                      email=self.customer.email,
                                                      password=self.customer.password,
                                                      password_confirm=self.customer.password)
        contact_information = self.luma_account_page.get_text_from_contact_information()

        assert self.customer.first_name in contact_information
        assert self.customer.last_name in contact_information
        assert self.customer.email in contact_information

    def generate_empty_field_data(self, customer: Customer, empty_fields: dict) -> Customer:
        for field_name, value in empty_fields.items():
            if field_name == "first_name" and value:
                customer.set_first_name("")
            elif field_name == "last_name" and value:
                customer.set_last_name("")
            elif field_name == "email" and value:
                customer.set_email("")
            elif field_name == "password" and value:
                customer.set_password("")
            elif field_name == "confirm_password" and value:
                customer.set_confirm_password("")
            else:
                print("Wrong key")

        return customer

    @pytest.mark.usefixtures("Attach screenshot when test is failed",
                             "Customer creation fixture",
                             "Go to luma test shop",
                             "Logout user from luma shop before test")
    @allure.sub_suite("01 Registration suite")
    @allure.description("Test of creating new user by using empty field data for luma test shop")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("02 Register user using empty field data")
    @pytest.mark.parametrize("first_name_is_empty", [True, False])
    @pytest.mark.parametrize("last_name_is_empty", [True, False])
    @pytest.mark.parametrize("email_is_empty", [True, False])
    @pytest.mark.parametrize("password_is_empty", [True, False])
    @pytest.mark.parametrize("confirm_password_is_empty", [True, False])
    def test_register_new_user_using_empty_field_data(self, first_name_is_empty, last_name_is_empty,
                                                      email_is_empty, password_is_empty, confirm_password_is_empty):
        if not first_name_is_empty \
                and not last_name_is_empty \
                and not email_is_empty \
                and not password_is_empty \
                and not confirm_password_is_empty:
            pytest.skip('This test is duplicate of "01 Registration test using valid data"')

        empty_fields = {"first_name": first_name_is_empty,
                        "last_name": last_name_is_empty,
                        "email": email_is_empty,
                        "password": password_is_empty,
                        "confirm_password": confirm_password_is_empty}

        customer_with_empty_field: Customer = self.generate_empty_field_data(self.customer, empty_fields)

        self.luma_home_page.click_create_account_button()

        self.luma_new_customer_page.register_new_user(
            first_name=customer_with_empty_field.first_name,
            last_name=customer_with_empty_field.last_name,
            email=customer_with_empty_field.email,
            password=customer_with_empty_field.password,
            password_confirm=customer_with_empty_field.confirm_password
        )

        true_keys = [key for key, value in empty_fields.items() if value]

        for field_to_check in true_keys:
            self.luma_new_customer_page.check_error_in_field(field=field_to_check)
