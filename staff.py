from person import Person

class Staff(Person):
    """
    Represents a hospital staff member.

    Inherits from the `Person` class and adds specific attributes and methods
    relevant to hospital staff.

    Attributes:
        name (str): The full name of the staff member.
        age (int): The age of the staff member.
        position (str): The job title or role of the staff member in the hospital.
    """
    def __init__(self, name: str, age: int, position: str) -> None:
        """
        Initialize a Staff object.

        Args:
            name (str): Name of the staff member.
            age (int): Age of the staff member.
            position (str): Job title or position of the staff member.
            
        """
        super().__init__(name, age)
        self.position = position
        
    def __str__(self) -> str:
        """
        User-friendly string representation of the Staff object.
        """
        return f"{self.name}, Age: {self.age}, Position: {self.position}"

    def __repr__(self) -> str:
        """
        Official string representation of the Staff object (for debugging).
        """
        return f"Staff(name={self.name!r}, age={self.age!r}, position={self.position!r})"


    def view_info(self) -> str:
        """
        Return a formatted string containing staff information.

        Returns:
            str: A human-readable summary of the staff member.
            
        """
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"
    