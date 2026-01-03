class Person:
    """
    Base class representing a person in the hospital system.

    This class stores common attributes shared by all people in the hospital,
    such as name and age. It also provides basic methods for displaying
    personal information. This class is intended to be inherited by
    other classes like Patient and Staff.

    Attributes:
        name (str): The name of the person. Cannot be empty or whitespace.
        age (int): The age of the person. Must be a non-negative integer.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.

        Raises:
            TypeError: If name is not a string or age is not an integer.
            ValueError: If name is empty/whitespace or age is negative.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty or whitespace")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")

        self.name = name.strip()
        self.age = age

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the person.

        Returns:
            str: A formatted string containing the person's name and age.
        """
        return f"Person Name: {self.name}, Age: {self.age}"

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the person.

        Returns:
            str: A detailed string representation of the person object.
        """
        return f"Person(name={self.name!r}, age={self.age})"

    def view_info(self) -> str:
        """
        View basic information about the person.

        Returns:
            str: A formatted string containing the person's basic information.
        """
        return f"Name: {self.name}, Age: {self.age}"
