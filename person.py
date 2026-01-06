from datetime import date


class Person:
    """
    Base class representing a person in the hospital system.

    This class stores core identity information shared by all individuals
    within the hospital system, including patients and staff members.
    It provides validated access to personal data and common utility
    methods. This class is intended to be inherited by more specialized
    classes such as Patient and Staff.

    Attributes:
        name (str): Full legal name of the person. Cannot be empty.
        date_of_birth (date): The person's date of birth.
    """

    def __init__(self, name: str, date_of_birth: date) -> None:
        """
        Initialize a Person object.

        Args:
            name (str): The full legal name of the person.
            date_of_birth (date): The person's date of birth.

        Raises:
            ValueError: If the name is empty or date_of_birth is in the future.
            TypeError: If date_of_birth is not a date object.
        """
        if not name:
            raise ValueError("Name cannot be empty")

        if not isinstance(date_of_birth, date):
            raise TypeError("date_of_birth must be a datetime.date instance")

        if date_of_birth > date.today():
            raise ValueError("Date of birth cannot be in the future")

        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the person.

        Returns:
            str: A formatted string containing the person's name and age.
        """
        return f"Name: {self.name}, Age: {self.get_age()}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the person for debugging.

        Returns:
            str: A precise representation suitable for debugging.
        """
        return (
            f"Person(name={self.name!r}, "
            f"date_of_birth={self.date_of_birth!r})"
        )

    def get_age(self) -> int:
        """
        Calculate the person's current age in years.

        The age is calculated dynamically from the date of birth to
        ensure accuracy for legal and medical use.

        Returns:
            int: The person's current age.
        """
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1

        return age

    def is_adult(self) -> bool:
        """
        Determine whether the person is legally an adult.

        Returns:
            bool: True if the person is 18 years or older, False otherwise.
        """
        return self.get_age() >= 18

    def update_name(self, new_name: str) -> None:
        """
        Update the person's name.

        Args:
            new_name (str): The new name to assign.

        Raises:
            ValueError: If the new name is empty.
        """
        if not new_name:
            raise ValueError("Name cannot be empty")
        self.name = new_name

    def to_dict(self) -> dict:
        """
        Convert the person's information into a dictionary format.

        This method is useful for database storage, serialization,
        and API communication.

        Returns:
            dict: A dictionary containing the person's data.
        """
        return {
            "name": self.name,
            "date_of_birth": self.date_of_birth.isoformat(),
            "age": self.get_age(),
        }
