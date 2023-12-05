class Rectangle(BaseGeometry):
    """Represents a rectangle with private instance attributes:
    - width
    - height

    Inherits from BaseGeometry and contains a public method area().
    """

    def __init__(self, width, height):
        """Initializes an instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string representing the Rectangle."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the rectangle instance.

        Overwrites the area() method from BaseGeometry.
        Returns:
            int: The computed area of the rectangle.
        """
        return self.__width * self.__height
