from datetime import date

class Person:
    """
    Base class representing a person in the hospital system.

    This class stores fundamental information shared by all
    individuals within the hospital, such as patients and staff.
    It ensures validated input for personal data and provides
    utility methods for accessing age, adulthood status, and
    formatted display of information.

    Attributes:
        name (str): Full legal name of the person. Cannot be empty.
        date_of_birth (date): The person's date of birth.
    """

    def __init__(self, name: str, date_of_birth: date) -> None:
        """
        Initialize a Person object with name and date of birth.

        Args:
            name (str): Full legal name of the person.
            date_of_birth (date): Date of birth of the person.

        Raises:
            ValueError: If the name is empty or date_of_birth is in the future.
            TypeError: If date_of_birth is not a datetime.date instance.
        """
        if not name or not name.strip():
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
            str: Formatted string with name and age.
        """
        return f"Name: {self.name}, Age: {self.get_age()}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the person
        suitable for debugging.

        Returns:
            str: Developer-friendly string with full initialization data.
        """
        return f"Person(name={self.name!r}, date_of_birth={self.date_of_birth!r})"

    def get_age(self) -> int:
        """
        Calculate the person's current age in years.

        The age is dynamically calculated based on today's date
        and the person's date of birth.

        Returns:
            int: The current age of the person.
        """
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def is_adult(self) -> bool:
        """
        Determine whether the person is legally an adult.

        Returns:
            bool: True if the person is 18 years or older, False otherwise.
        """
        return self.get_age() >= 18

    def view_info(self) -> str:
        """
        Provide a readable summary of the person's basic information.

        Returns:
            str: Name and age of the person in a formatted string.
        """
        return f"Name: {self.name}, Age: {self.get_age()}"
