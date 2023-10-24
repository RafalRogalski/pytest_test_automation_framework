from resources.base import Base
from resources.variables import Variables as Tv


class AllureHelper(Base):

    def __init__(self, folder_location):
        super().__init__()
        self.__folder_location = folder_location
        self.__browser_name = "Chrome"
        self.__browser_version = self.driver.capabilities['browserVersion']
        self.__stand = "Production"

        self.__report_raw_location = r"report/report_raw/environment.properties"
        self.__environment_str = ""
        self._set_environment_str()

    def create_environment_file(self):
        with open(f"{self.__folder_location}/{self.__report_raw_location}", "w+") as file:
            print(self.__report_raw_location)
            print(self.__environment_str)
            file.write(self.__environment_str)
            print(file.read())

    def _set_environment_str(self):
        self.__environment_str = f"Browser = {self.__browser_name}\n" \
                                 f"Browser_version = {self.__browser_version}\n" \
                                 f"Stand = {self.__stand}\n"
