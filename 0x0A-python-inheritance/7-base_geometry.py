#!/usr/bin/python3
"""
Defines a class BaseGeometry
"""


class BaseGeometry():
    """
    BaseGeometry class
    """
    def area(self):
        """
        Method not implemented
        Raises:
            Exception if method is called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the parameter 'value'
        Args:
            name (str): name of value
            value (int)
        Raises:
            TypeError if value is not an integer
            ValueError if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
