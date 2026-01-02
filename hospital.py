from department import Department
class Hospital:
    """
    Class for managing hospital operations and its departments.

    Attributes:
        name (str): The name of the hospital.
        location (str): The physical address or city of the hospital.
        departments (list): A list of Department objects associated with the hospital.
    """

    def __init__(self, name: str, location: str) -> None:
        """
        Initialize a Hospital object.

        Args:
            name (str): Name of the hospital.
            location (str): Location of the hospital.
        """
        self.name = name
        self.location = location
        self.departments = []  # List to hold Department objects
        
    def __str__(self) -> str:
        """
        User-friendly string representation.
        Summarizes the hospital and the count of departments.
        """
        dept_count = len(self.departments)
        return (f"Hospital: {self.name} | Location: {self.location} "
                f"| Departments: {dept_count}")

    def __repr__(self) -> str:
        """
        Official string representation for debugging.
        Shows the state required to recreate the object.
        """
        return f"Hospital(name={self.name!r}, location={self.location!r}, departments={self.departments!r})"

    def add_department(self, department : Department) -> None:
        """
        Add a department to the hospital.

        Args:
            department (Department): The Department instance to be added.
        """
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")

    