#!/usr/bin/python3
"""Defines a class Square."""

class Square:
	"""Represents a square."""

	def __init__(self, size):
		"""Initializes a new square.
		
		Args:
		    size (int): The size of the new square.
		"""
		self.size = size

	@property
	def size(self):
		"""Gets/sets the current size of the square."""
		return (self.__size)

	@size.setter
	def size(self, value):
		"""Sets the size of the square.

		Args:
		    value (int): The size to set for the square.
		
		Raises:
		    TypeError: If the value is not an integer.
		    ValueError: If the value is negative.
		"""
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	def area(self):
		"""Returns the current area of the square."""
		return (self.__size * self.__size)

	def my_print(self):
		"""Prints the square with the # character."""
		i = 0
		while i < self.__size:
			j = 0
			while j < self.__size:
				print("#", end="")
				j += 1
			print("")
			i += 1
		if self.__size == 0:
			print("")
