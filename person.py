class Person:
    """
    Base class representing a person in the hospital system.

    This class stores common attributes shared by all people in the hospital,
    such as name and age. It also provides basic methods for displaying
    personal information. This class is intended to be inherited by
    other classes like Patient and Staff.

    Attributes:
        name (str): The name of the person. Cannot be empty.
        age (int): The age of the person.
    """
    
    def __init__(self, name : str, age : int)-> None:
        """
        Initialize a Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.

        Raises:
            ValueError: If the name is empty or age is negative.
            TypeError: If age is not an integer.
        """
        if not name:
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        self.name = name
        self.age = age
        
    def __str__(self)-> str:
        """
        Return a user-friendly string representation of the person.

        Returns:
            str: A formatted string containing the person's name and age.
        """
        return f"Person Name : {self.name} , person Age: {self.age}"
    
    def __repr__(self)-> str:
        """
        Return a string representation of the person object for debugging.

        Returns:
            str: A detailed string representation of the person object.
        """
        return f"Person Name : {self.name} , person Age: {self.age}"

    def view_info(self)-> str:
        """
        View basic information about the person.

        Returns:
            str: A formatted string containing the person's basic information.
        """
        return f"Person Name : {self.name} , person Age: {self.age}"