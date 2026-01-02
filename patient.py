from person import Person
class Patient(Person):
    """
    Represents a hospital patient.

    This class extends the Person class by adding medical
    record information specific to patients. It is used
    to store and manage patient-related data in the
    hospital system.

    Attributes:
        medical_record (str): The patient's medical record.
            Cannot be empty.
    """
    def __init__(self, name : str, age : int, medical_record : str)-> None:
        """
        Initialize a Patient object.

        Args:
            name (str): The name of the patient.
            age (int): The age of the patient.
            medical_record (str): The patient's medical record.

        Raises:
            ValueError: If the medical record is empty.
        """
        super().__init__(name, age)
        if not medical_record or not medical_record.strip():
            raise ValueError("Medical record cannot be empty")
        self.medical_record = medical_record
        
    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the patient.
        """
        return f"{super().__str__()}, Medical Record: {self.medical_record}"

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the patient.
        """
        return (
            f"Patient(name={self.name!r}, "
            f"age={self.age}, "
            f"medical_record={self.medical_record!r})"
        )

    def view_record(self)-> str:
        """
        View the patient's medical record.

        Returns:
            str: A formatted string containing the patient's
            medical record information.
        """
        return f"Medical Record for {self.name}: {self.medical_record}"