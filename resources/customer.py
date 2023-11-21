from faker import Faker


class Customer:
    """This class is created for luma test shop with unique data"""

    def __init__(self):
        self._fake = Faker()
        self.first_name = self._fake.first_name()
        self.last_name = self._fake.last_name()
        self.email = self._fake.email()
        self.password = self._fake.password()
        self.confirm_password = self.password

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_email(self, new_email):
        self.email = new_email

    def set_password(self, new_password):
        self.password = new_password

    def set_confirm_password(self, new_confirm_password):
        self.confirm_password = new_confirm_password
