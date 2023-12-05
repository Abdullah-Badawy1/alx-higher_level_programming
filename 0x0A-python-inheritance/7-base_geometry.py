class BaseGeometry:
    """A class with public instance methods for geometric operations."""

    def area(self):
        """Raises an Exception indicating 'area() is not implemented'."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value passed as an integer.

        Args:
            name: A string indicating the name associated with the value.
            value: An integer value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
