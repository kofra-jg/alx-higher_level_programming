#!/usr/bin/python3
"""A simple module to define a ``Rectangle``
"""


class Rectangle:
    """A simple ``Rectangle`` class"""
    def __init__(self, width=0, height=0):
        """Constructs a ``Rectangle`` object

        Args:
            width (`int`): The ``width`` of the ``Rectangle``
                 height (`int`): The ``height`` of the ``Rectangle``
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Args:
            height (`int`): The height of the ``Rectangle``
        Raises:
            TypeError: if ``height`` is not an integer
            ValueError: if ``height`` < 0
        """
        return self._Rectangle__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = height

    @property
    def width(self):
        """
        Args:
            width (`int`): The width of the ``Rectangle``
        Raises:
            TypeError: if ``width`` is not an integer
            ValueError: if ``width`` < 0
        """
        return self._Rectangle__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = width

    def area(self):
        """Computes the ``area`` of the ``Rectangle``"""
        return self.width * self.height

    def perimeter(self):
        """Computes the ``perimeter`` of the ``Rectangle``"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
