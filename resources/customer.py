from faker import Faker


class Customer:
    """This class is created for luma test shop with unique data"""

    def __init__(self):
        self._fake = Faker()
        self.first_name = self._fake.first_name()
        self.last_name = self._fake.last_name()
        self.email = self._fake.email()
        self.password = self._fake.password()
