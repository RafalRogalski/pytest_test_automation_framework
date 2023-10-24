from abc import ABC, abstractmethod

from selenium.webdriver.remote.webelement import WebElement

# Library to draw rectangle on screenshot
import io
from PIL import Image, ImageDraw
from io import BytesIO


class Shape(ABC):

    @abstractmethod
    def area_points(self):
        pass


class Rectangle(Shape):
    def __init__(self, element: WebElement):
        self._element = element

    def area_points(self) -> tuple:
        """Method to get info where the red rectangle should be drawn on screenshot"""
        x_start = self._element.location['x']
        y_start = self._element.location['y']
        x_end = self._element.size['width'] + x_start
        y_end = self._element.size['height'] + y_start
        return x_start, y_start, x_end, y_end


class Polygon(Shape):
    def __init__(self, element: WebElement):
        self._element = element

    def area_points(self) -> list:
        """Method that returns list of points for red arrow near rectangle"""
        x_start = self._element.size['width'] + self._element.location['x'] + 6
        y_start = (self._element.size['height'] / 2) + self._element.location['y']
        polygon_points = [(x_start, y_start), (x_start + 10, y_start - 10), (x_start + 10, y_start + 10)]
        return polygon_points


class ScreenshotDrawer:
    """Class that is responsible for drawing rectangle and arrow on taken screenshot"""

    def __init__(self, element, screenshot):
        self._element = element
        self._screenshot = screenshot

    def get_screenshot(self) -> object:
        """Method takes screenshot and draws rectangle on element we are looking for with arrow on right in the middle
        :return: screenshot as bytes object fit for allure.attach method in jpg
        """

        img = Image.open(BytesIO(self._screenshot))
        img = img.convert('RGB')
        draw = ImageDraw.Draw(img)

        rectangle_points = Rectangle(self._element).area_points()
        polygon_points = Polygon(self._element).area_points()

        draw.rectangle(rectangle_points, outline="red", width=3)
        draw.polygon(polygon_points, fill='red')

        img_bytes = io.BytesIO()
        img.save(img_bytes, "JPEG")

        return img_bytes.getvalue()
